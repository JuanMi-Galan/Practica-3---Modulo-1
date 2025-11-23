"""
Módulo de utilidades para análisis de datos.

Incluye funciones con tipado estático.
"""

from typing import Any, Dict, List, Optional, Tuple, Union

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from ctg_viz.preprocessing import columnas_float_enteras
from ctg_viz.categorization import clasificar_columnas_continuas_discretas

from ctg_viz.plots.histograms import plot_histograms
from ctg_viz.plots.boxplots import plot_boxplots
from ctg_viz.plots.barplots import plot_barplots
from ctg_viz.plots.density import plot_density
from ctg_viz.plots.heatmap import plot_heatmap, compute_spearman_corr
from ctg_viz.plots.lineas import plot_lineplots
from ctg_viz.plots.dotplot import plot_dotplots
from ctg_viz.plots.violin import plot_violins

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


def analyze_outliers_impact(
    data: pd.DataFrame,
    column: str,
    outliers_indices: Union[pd.Index, List[int]],
) -> Tuple[pd.Series, pd.DataFrame]:
    """Analiza el impacto de los outliers en estadísticas descriptivas básicas.

    Calcula media, mediana, desviación estándar, mínimo y máximo antes
    y después de eliminar los outliers.

    Args:
        data:
            DataFrame original con la columna numérica.
        column:
            Nombre de la columna a analizar.
        outliers_indices:
            Índices de filas considerados outliers (por ejemplo,
            los devueltos por ``detect_outliers_comprehensive``).

    Returns:
        Tuple:
            - Serie sin outliers.
            - DataFrame con las estadísticas antes y después
              de eliminar los outliers.
    """
    original_data: pd.Series = data[column].dropna()

    if isinstance(outliers_indices, pd.Index):
        indices_list = outliers_indices.tolist()
    else:
        indices_list = list(outliers_indices)

    clean_data: pd.Series = original_data.drop(index=indices_list, errors="ignore")

    stats_comparison = pd.DataFrame(
        {
            "Con_Outliers": [
                original_data.mean(),
                original_data.median(),
                original_data.std(),
                original_data.min(),
                original_data.max(),
            ],
            "Sin_Outliers": [
                clean_data.mean(),
                clean_data.median(),
                clean_data.std(),
                clean_data.min(),
                clean_data.max(),
            ],
        },
        index=["Media", "Mediana", "Desv_Estándar", "Mínimo", "Máximo"],
    )

    stats_comparison["Diferencia_Abs"] = (
        stats_comparison["Sin_Outliers"] - stats_comparison["Con_Outliers"]
    ).abs()

    stats_comparison["Cambio_Porcentual"] = (
        (stats_comparison["Sin_Outliers"] - stats_comparison["Con_Outliers"])
        / stats_comparison["Con_Outliers"]
        * 100
    ).round(2)

    print("ANÁLISIS DEL IMPACTO DE OUTLIERS")
    print(stats_comparison)

    return clean_data, stats_comparison

# PRUEBAS

def test_clasificacion_continua_discreta_alta_cardinalidad():
    '''
    Prueba de la funcion, maracar correcatamente la clasificación definida
    '''
    # DataFrame de prueba con los 3 tipos
    df = pd.DataFrame({
        # CONTINUA: más de 10 valores únicos y numérica
        "edad": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110],

        # DISCRETA: 10 o menos valores únicos
        "genero": ["M", "F", "M", "F", "M", "F", "M", "F", "M", "F", "M"],

        # ALTA CARDINALIDAD: no numérica, más de 10 valores
        "nombre": [
            "Ana", "Luis", "Pedro", "Maria", "Jose", "Sandra", 
            "Karla", "Eli", "Leo", "Nora", "Diana"
        ],

        # FECHA → ALTA CARDINALIDAD
        "fecha_compra": pd.date_range("2021-01-01", periods=11)
    })

    resultado = clasificar_columnas_continuas_discretas(df)

    # --- Validación de CONTINUAS ---
    assert "edad" in resultado["continuas"]
    assert "genero" not in resultado["continuas"]
    assert "nombre" not in resultado["continuas"]
    assert "fecha_compra" not in resultado["continuas"]

    # --- Validación de DISCRETAS ---
    assert "genero" in resultado["discretas"]
    assert "edad" not in resultado["discretas"]
    assert "nombre" not in resultado["discretas"]
    assert "fecha_compra" not in resultado["discretas"]

    # --- Validación de ALTA CARDINALIDAD ---
    assert "nombre" in resultado["alta_cardinalidad"]
    assert "fecha_compra" in resultado["alta_cardinalidad"]
    assert "edad" not in resultado["alta_cardinalidad"]
    assert "genero" not in resultado["alta_cardinalidad"]

def test_columnas_float_enteras_normal():
    '''
    Prueba de la funcion, marcar correctamente las columnas que son floats,
    si son enteros o si son float
    '''
    df = pd.DataFrame({
        "solo_enteros": [1.0, 2.0, 3.0, np.nan],
        "con_decimales": [1.2, 2.0, 3.5, np.nan],
        "entera_int": [1, 2, 3, 4],  # No se debe analizar
    })

    resultado = columnas_float_enteras(df)

    assert resultado["enteras"] == ["solo_enteros"]
    assert resultado["decimales"] == ["con_decimales"]

def test_detect_outliers_iqr_simple():
    """Debe detectar el 100 como outlier con IQR."""
    serie = pd.Series([1, 1, 1, 1, 100], name="x")

    detalles = detect_outliers(
        data=serie,
        methods=["iqr"],
        plot=False,
        return_details=True,
    )

    # detalles es un dict con 3 claves: results, indices, common
    resultados = detalles["results"]
    indices = detalles["indices"]

    assert resultados["iqr"]["outliers_count"] == 1
    assert list(resultados["iqr"]["outliers_values"]) == [100]
    assert indices["iqr"] == [4]

def test_detect_outliers_dataframe_column():
    """Debe funcionar igual usando DataFrame y especificando columna."""
    df = pd.DataFrame({"x": [1, 1, 1, 1, 100]})

    resultados = detect_outliers(
        data=df,
        column="x",
        methods=["iqr"],
        plot=False,
        return_details=False,
    )

    assert resultados["iqr"]["outliers_count"] == 1


def test_modified_zscore_no_division_by_zero():
    """No debe fallar cuando todos los valores son iguales (MAD = 0)."""
    serie = pd.Series([5, 5, 5, 5, 5], name="constante")

    resultados = detect_outliers(
        data=serie,
        methods=["modified_zscore"],
        plot=False,
        return_details=False,
    )

    # Con todos los valores iguales, no debería haber outliers.
    assert resultados["modified_zscore"]["outliers_count"] == 0


def test_analyze_outliers_impact_reduces_max():
    """Al quitar un outlier grande, el máximo debe disminuir."""
    df = pd.DataFrame({"x": [1, 2, 3, 4, 100]})
    # Simulamos que el índice 4 (valor 100) es un outlier
    outlier_indices = [4]

    serie_limpia, stats_comp = analyze_outliers_impact(df, "x", outlier_indices)

    assert serie_limpia.max() == 4
    assert stats_comp.loc["Máximo", "Con_Outliers"] == 100
    assert stats_comp.loc["Máximo", "Sin_Outliers"] == 4

def _dummy_ctg_df() -> pd.DataFrame:
    """Crea un DataFrame pequeño similar al de CTG para pruebas."""
    n = 20
    data = {
        "FileName": [f"f_{i}" for i in range(n)],
        "Date": pd.date_range("2020-01-01", periods=n, freq="D"),
        "SegFile": np.arange(n),
        "ASTV": np.random.uniform(0, 100, size=n),
        "MSTV": np.random.uniform(0, 10, size=n),
        "Width": np.random.uniform(20, 60, size=n),
        "Mean": np.random.uniform(100, 200, size=n),
        "Variance": np.random.uniform(0, 50, size=n),
        "CLASS": np.random.choice([1, 2, 3], size=n),
        "NSP": np.random.choice([1, 2, 3], size=n),
    }
    return pd.DataFrame(data)


def test_plot_histograms_individual():
    """plot_histograms debe ejecutar sin errores y devolver el mismo shape."""
    df = _dummy_ctg_df()
    plot_histograms(df, target_col="NSP", show=False)


def test_plot_boxplots_individual():
    """plot_boxplots debe ejecutar sin errores y devolver el mismo shape."""
    df = _dummy_ctg_df()
    plot_boxplots(df, target_col="NSP", show=False)


def test_plot_barplots_individual():
    """plot_barplots debe ejecutar sin errores y devolver el mismo shape."""
    df = _dummy_ctg_df()
    plot_barplots(df, show=False)


def test_plot_density_individual():
    """plot_density debe ejecutar sin errores y devolver el mismo shape."""
    df = _dummy_ctg_df()
    plot_density(df, target_col="NSP", show=False)


def test_compute_spearman_corr_individual():
    """compute_spearman_corr debe devolver una matriz cuadrada con numéricas."""
    df = _dummy_ctg_df()
    corr = compute_spearman_corr(df)

    assert isinstance(corr, pd.DataFrame)
    # Debe ser cuadrada
    assert corr.shape[0] == corr.shape[1]

    numeric_cols = df.select_dtypes(include=["number"]).columns
    assert set(corr.columns) == set(numeric_cols)
    assert set(corr.index) == set(numeric_cols)


def test_plot_heatmap_individual():
    """plot_heatmap debe ejecutar sin errores y devolver el mismo shape."""
    df = _dummy_ctg_df()
    plot_heatmap(df, show=False)

def _dummy_df() -> pd.DataFrame:
    n = 20
    data = {
        "SegFile": np.arange(n),
        "ASTV": np.random.uniform(0, 100, size=n),
        "MSTV": np.random.uniform(0, 10, size=n),
        "Width": np.random.uniform(20, 60, size=n),
        "NSP": np.random.choice([1, 2, 3], size=n),
    }
    return pd.DataFrame(data)

def test_plot_lineplots_individual():
    df = _dummy_df()
    plot_lineplots(df, time_col="SegFile", show=False)


def test_plot_dotplots_individual():
    df = _dummy_df()
    plot_dotplots(df, target_col="NSP", show=False)


def test_plot_violins_individual():
    df = _dummy_df()
    plot_violins(df, target_col="NSP", show=False)