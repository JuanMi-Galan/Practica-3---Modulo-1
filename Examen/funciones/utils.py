"""
Módulo de utilidades para análisis de datos.

Incluye funciones con tipado estático.
"""
from typing import Any, Dict, List, Optional, Tuple, Union

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# FUNCIONES

OutlierResults = Dict[str, Any]
OutlierIndices = Dict[str, List[int]]


def detect_outliers(
    data: Union[pd.Series, pd.DataFrame],
    column: Optional[str] = None,
    methods: Optional[List[str]] = None,
    z_threshold: float = 3.0,
    iqr_factor: float = 1.5,
    plot: bool = True,
    return_details: bool = False,
) -> Union[OutlierResults, Tuple[OutlierResults, OutlierIndices]]:
    """Detecta outliers univariados utilizando varios métodos sencillos.

    Métodos disponibles:
      - ``"iqr"``: rango intercuartílico.
      - ``"zscore"``: Z-score clásico.
      - ``"modified_zscore"``: Z-score modificado basado en MAD.

    Args:
        data:
            Serie o DataFrame con los datos numéricos.
        column:
            Nombre de la columna si ``data`` es un DataFrame.
        methods:
            Lista de métodos a usar. Si es None, se utilizan
            ``["iqr", "zscore", "modified_zscore"]``.
        z_threshold:
            Umbral para considerar un valor como outlier
            en Z-score y Z-score modificado.
        iqr_factor:
            Factor multiplicador del IQR para definir los límites
            inferior y superior: [Q1 - k·IQR, Q3 + k·IQR].
        plot:
            Si es True, genera visualizaciones básicas.
        return_details:
            Si es True, devuelve también los índices de outliers
            por método.

    Returns:
        Si ``return_details`` es False:
            Dict con las estadísticas de outliers por método.
        Si ``return_details`` es True:
            Tuple (resultados, outlier_indices), donde:
            - resultados: dict con estadísticas por método.
            - outlier_indices: dict con índices de outliers por método.

    Raises:
        ValueError:
            Si ``data`` es un DataFrame y no se especifica ``column``.
    """
    # 1. Preparar la serie numérica base
    if isinstance(data, pd.DataFrame):
        if column is None:
            raise ValueError("Especifica el nombre de la columna cuando 'data' es un DataFrame.")
        series: pd.Series = data[column].dropna()
        data_name: str = column
    else:
        series = data.dropna()
        data_name = series.name if series.name else "Variable"

    if methods is None:
        methods = ["iqr", "zscore", "modified_zscore"]

    results: OutlierResults = {}
    outlier_indices: OutlierIndices = {}

    # 2. Método IQR
    if "iqr" in methods:
        q1: float = float(series.quantile(0.25))
        q3: float = float(series.quantile(0.75))
        iqr: float = q3 - q1

        lower_bound: float = q1 - iqr_factor * iqr
        upper_bound: float = q3 + iqr_factor * iqr

        iqr_outliers: pd.Series = series[(series < lower_bound) | (series > upper_bound)]
        outlier_indices["iqr"] = iqr_outliers.index.tolist()

        results["iqr"] = {
            "method": "IQR",
            "outliers_count": int(len(iqr_outliers)),
            "outliers_percentage": float(len(iqr_outliers) / len(series) * 100),
            "lower_bound": lower_bound,
            "upper_bound": upper_bound,
            "outliers_values": iqr_outliers.values,
            "outliers_indices": iqr_outliers.index.tolist(),
        }

    # 3. Método Z-score clásico
    if "zscore" in methods:
        # stats.zscore devuelve un array de floats (puede incluir NaN si todo es constante)
        z_scores_array: np.ndarray = stats.zscore(series, nan_policy="omit")
        z_scores = np.abs(z_scores_array)

        zscore_outliers: pd.Series = series[z_scores > z_threshold]
        outlier_indices["zscore"] = zscore_outliers.index.tolist()

        results["zscore"] = {
            "method": "Z-score",
            "outliers_count": int(len(zscore_outliers)),
            "outliers_percentage": float(len(zscore_outliers) / len(series) * 100),
            "threshold": z_threshold,
            "outliers_values": zscore_outliers.values,
            "outliers_indices": zscore_outliers.index.tolist(),
            "z_scores": z_scores[z_scores > z_threshold],
        }

    # 4. Método Z-score modificado (MAD)
    if "modified_zscore" in methods:
        median: float = float(series.median())
        mad: float = float(np.median(np.abs(series - median)))  # Median Absolute Deviation

        # Evitar división entre cero si todos los valores son iguales
        if mad == 0:
            modified_z_scores = np.zeros_like(series, dtype=float)
        else:
            modified_z_scores = 0.6745 * (series - median) / mad

        abs_mod_z = np.abs(modified_z_scores)
        mad_outliers: pd.Series = series[abs_mod_z > z_threshold]
        outlier_indices["modified_zscore"] = mad_outliers.index.tolist()

        results["modified_zscore"] = {
            "method": "Modified Z-score (MAD)",
            "outliers_count": int(len(mad_outliers)),
            "outliers_percentage": float(len(mad_outliers) / len(series) * 100),
            "threshold": z_threshold,
            "outliers_values": mad_outliers.values,
            "outliers_indices": mad_outliers.index.tolist(),
            "modified_z_scores": abs_mod_z[abs_mod_z > z_threshold],
        }

    # 5. Visualizaciones
    if plot:
        _plot_outliers(series=series,
                       data_name=data_name,
                       results=results,
                       methods=methods,
                       z_threshold=z_threshold)

    # 6. Resumen en texto
    print(f"RESUMEN DE DETECCIÓN DE OUTLIERS - {data_name}")
    for method_key in methods:
        if method_key in results:
            result = results[method_key]
            print(f"{result['method']}:")
            print(f"   • Outliers detectados: {result['outliers_count']}")
            print(f"   • Porcentaje: {result['outliers_percentage']:.2f}%")
            if method_key == "iqr":
                print(f"   • Límite inferior: {result['lower_bound']:.2f}")
                print(f"   • Límite superior: {result['upper_bound']:.2f}")
            elif method_key in ("zscore", "modified_zscore"):
                print(f"   • Umbral utilizado: {result['threshold']}")
            print()

    # Inicializar por defecto
    common_sorted = []

    # 7. Outliers comunes a todos los métodos utilizados
    if len(methods) > 1:
        valid_methods = [m for m in methods if m in outlier_indices]

        if valid_methods:
            common = set(outlier_indices[valid_methods[0]])
            for m in valid_methods[1:]:
                common = common.intersection(set(outlier_indices[m]))

            print(f"Outliers detectados por TODOS los métodos usados: {len(common)}")

            if common:
                common_sorted = sorted(common)  # ahora sí tiene valor real
                common_values = [series.loc[idx] for idx in common_sorted]
                print(f"   Índices: {common_sorted}")
                print(f"   Valores: {common_values}")
                print(f"   Valores únicos: {sorted(set(common_values))}")
                print()

    if return_details:
        return {
            "results": results,
            "indices": outlier_indices,
            "common": common_sorted
        }

    return results

def _plot_outliers(
    series: pd.Series,
    data_name: str,
    results: OutlierResults,
    methods: List[str],
    z_threshold: float,
) -> None:
    """Genera gráficos simples para visualizar outliers.

    Args:
        series:
            Serie numérica analizada.
        data_name:
            Nombre legible de la variable.
        results:
            Resultados por método.
        methods:
            Lista de métodos utilizados.
        z_threshold:
            Umbral de Z-score para las líneas de referencia.
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle(f"Detección de Outliers - {data_name}", fontsize=16, fontweight='bold')

    # 1. Boxplot
    ax1 = axes[0, 0]
    ax1.boxplot(series, patch_artist=True, notch=True)
    ax1.set_title("Boxplot (IQR)")
    ax1.set_ylabel("Valores")
    ax1.grid(True, alpha=0.3)

    # 2. Histograma con outliers IQR (si existen)
    ax2 = axes[0, 1]
    ax2.hist(series, bins=50, alpha=0.7, color='skyblue', edgecolor="black")
    if "iqr" in results:
        for outlier in results["iqr"]["outliers_values"]:
            ax2.axvline(outlier, color="red", alpha=0.6, linestyle="--")
    ax2.set_title("Histograma con outliers IQR")
    ax2.set_xlabel("Valores")
    ax2.set_ylabel("Frecuencia")
    ax2.grid(True, alpha=0.3)

    # 3. Z-scores (si se calculó)
    ax3 = axes[1, 0]
    if "zscore" in results:
        z_scores_array: np.ndarray = stats.zscore(series, nan_policy="omit")
        ax3.scatter(range(len(z_scores_array)), z_scores_array, alpha=0.6)
        ax3.axhline(y=z_threshold, color="red", linestyle="--", label=f"+{z_threshold}")
        ax3.axhline(y=-z_threshold, color="red", linestyle="--", label=f"-{z_threshold}")
        ax3.set_title("Z-scores")
        ax3.set_xlabel("Índice")
        ax3.set_ylabel("Z-score")
        ax3.legend()
        ax3.grid(True, alpha=0.3)
    else:
        ax3.axis("off")

    # 4. Comparación de métodos (número de outliers)
    ax4 = axes[1, 1]
    method_names: List[str] = []
    outlier_counts: List[int] = []
    outlier_percentages: List[float] = []

    for method_key in methods:
        if method_key in results:
            method_names.append(results[method_key]["method"])
            outlier_counts.append(results[method_key]["outliers_count"])
            outlier_percentages.append(results[method_key]["outliers_percentage"])

    if method_names:
        x_pos = np.arange(len(method_names))
        ax4.bar(
        x_pos,
        outlier_counts,
        alpha=0.7,
        color=['lightcoral', 'lightgreen', 'lightblue'][:len(method_names)]
        )

        for i, (count, pct) in enumerate(zip(outlier_counts, outlier_percentages)):
            ax4.text(
                i,
                count + max(outlier_counts) * 0.01,
                f"{pct:.1f}%",
                ha="center",
                va="bottom",
                fontweight="bold",
            )

        ax4.set_title("Comparación de métodos")
        ax4.set_xlabel("Método")
        ax4.set_ylabel("Número de outliers")
        ax4.set_xticks(x_pos)
        ax4.set_xticklabels(method_names, rotation=45, ha="right")
        ax4.grid(True, axis="y", alpha=0.3)
    else:
        ax4.axis("off")

    plt.tight_layout()
    plt.show()

def categorize_price(x):
    """
    Categoriza el precio numérico de un restaurante en niveles: "low", "medium" o "high".

    La función asigna una categoría según los siguientes rangos:
        - low:    precios menores o iguales a 20
        - medium: precios mayores a 20 y menores o iguales a 50
        - high:   precios mayores a 50

    Parameters
    ----------
    x : float or int
        Precio del restaurante.

    Returns
    -------
    str
        Una cadena con la categoría del precio: "low", "medium" o "high".

    Examples
    --------
    >>> categorize_price(15)
    'low'
    >>> categorize_price(40)
    'medium'
    >>> categorize_price(85)
    'high'
    """
    if x <= 20:
        return "low"
    elif x <= 50:
        return "medium"
    else:
        return "high"

def ambience_match(user_amb, rest_amb):
    """
    Clasifica el nivel de compatibilidad entre la preferencia del usuario y el ambiente del restaurante.
    Incluye manejo de valores desconocidos como '?', que se consideran 'no match'.

    Reglas:

    PERFECT MATCH:
        - user='family'   & restaurant='familiar'
        - user='solitary' & restaurant='quiet'

    COMPATIBLE:
        - user='friends'  compatible con ['familiar']
        - user='family'   compatible con ['quiet']
        - user='solitary' compatible con ['familiar']

    Cualquier valor desconocido (por ejemplo '?') o combinación no cubierta → 'no match'.

    Parameters
    ----------
    user_amb : str
        Preferencia de ambiente del usuario ('family', 'friends', 'solitary', '?').

    rest_amb : str
        Ambiente del restaurante ('familiar', 'quiet').

    Returns
    -------
    str
        Una de las siguientes etiquetas:
        - 'perfect match'
        - 'compatible'
        - 'no match'
    """

    user_amb = str(user_amb).lower()
    rest_amb = str(rest_amb).lower()

    # Manejar valores desconocidos
    if user_amb in ["?", "nan", "none", "null", "NaN"]:
        return "no match"

    # Perfect match
    perfect = {
        "family": "familiar",
        "solitary": "quiet"
    }

    if user_amb in perfect and perfect[user_amb] == rest_amb:
        return "perfect match"

    # Compatible
    compatible = {
        "friends": ["familiar"],
        "family": ["quiet"],
        "solitary": ["familiar"]
    }

    if user_amb in compatible and rest_amb in compatible[user_amb]:
        return "compatible"

    # No match
    return "no match"

def clean_null_strings(df):
    """
    Limpia valores nulos representados como texto y los convierte en NaN reales.
    
    Reemplaza valores como: '?', 'none', 'no', 'null', 'nan', '', ' ' 
    por NaN, sin importar la columna.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame a limpiar.

    Returns
    -------
    pandas.DataFrame
        DataFrame con los valores nulos estándar convertidos en np.nan.
    """

    null_values = [
        "?", "??",
        "none", "None", "NONE",
        "no", "No", "NO",
        "null", "Null", "NULL",
        "nan", "NaN", "NAN",
        "n/a", "N/A",
        "", " ", "  "
    ]

    # Convertir todo a string temporalmente para reemplazar
    df = df.map(lambda x: np.nan if str(x).strip() in null_values else x)

    return df