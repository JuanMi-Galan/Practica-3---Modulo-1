from typing import List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_lineplots(
    df: pd.DataFrame,
    time_col: str = "index",
    show: bool = True,
) -> None:
    """Genera gráficos de líneas para todas las columnas numéricas.

    La función simula una serie temporal ordenando por una columna de tiempo
    si existe; en caso contrario utiliza el índice.

    Para cada variable numérica se genera un gráfico de líneas independiente.

    Args:
        df: DataFrame de entrada.
        time_col: Nombre de la columna que se usará como eje X si existe.
        show: Si es True se muestran las figuras; si es False se cierran.

    Returns:
        None
    """
    sns.set(style="whitegrid")

    numeric_cols: List[str] = df.select_dtypes(include=["number"]).columns.tolist()

    # Determinar eje de tiempo (columna o índice)
    use_time_col: bool = time_col in df.columns

    if use_time_col:
        df_sorted = df.sort_values(by=time_col)
    else:
        df_sorted = df.sort_index()

    for col in numeric_cols:
        # Si usamos time_col en el eje X, no tiene sentido graficarlo también en Y
        if use_time_col and col == time_col:
            continue

        fig, ax = plt.subplots(figsize=(8, 4))

        if use_time_col:
            ax.plot(df_sorted[time_col], df_sorted[col], linestyle="-", marker="", alpha=0.8)
            ax.set_xlabel(time_col)
        else:
            ax.plot(df_sorted.index, df_sorted[col], linestyle="-", marker="", alpha=0.8)
            ax.set_xlabel("Fecha")

        ax.set_ylabel(col)
        ax.set_title(f"Serie de {col}")

        fig.tight_layout()

        if show:
            plt.show()
        else:
            plt.close(fig)

    return None
