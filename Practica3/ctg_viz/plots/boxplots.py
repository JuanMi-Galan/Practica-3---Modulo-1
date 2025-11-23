from typing import List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_boxplots(
    df: pd.DataFrame,
    target_col: str = "NSP",
    show: bool = True
) -> None:
    """
    Genera boxplots para todas las columnas numéricas.
    Si existe la columna objetivo, se generan boxplots por clase objetivo.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    target_col : str, optional
        Columna objetivo para agrupar en el eje X (por defecto "NSP").
    show : bool, optional
        Si True, muestra las figuras; si False, las cierra.

    Returns
    -------
    None
    """

    sns.set(style="whitegrid")
    numeric_cols: List[str] = df.select_dtypes(include=["number"]).columns.tolist()
    has_target: bool = target_col in df.columns

    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(6, 4))

        # Si existe la columna target, graficar por categoría
        if has_target:
            sns.boxplot(
                data=df,
                x=target_col,
                y=col,
                orient="v",  # evita warning por 'vert'
                ax=ax,
            )
            ax.set_title(f"Boxplot de {col} por {target_col}")

        else:
            sns.boxplot(
                data=df,
                y=col,
                orient="v",
                ax=ax,
            )
            ax.set_title(f"Boxplot de {col}")

        fig.tight_layout()

        if show:
            plt.show()
        else:
            plt.close(fig)

    return None
