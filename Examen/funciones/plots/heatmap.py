import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def compute_spearman_corr(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula la matriz de correlación de Spearman para todas las columnas numéricas.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.

    Returns
    -------
    pandas.DataFrame
        Matriz de correlación de Spearman.
    """
    numeric_df: pd.DataFrame = df.select_dtypes(include=["number"])
    corr: pd.DataFrame = numeric_df.corr(method="spearman")
    return corr


def plot_heatmap(df: pd.DataFrame, show: bool = True) -> None:
    """Genera un heatmap de correlaciones de Spearman para columnas numéricas."""

    sns.set(style="whitegrid")

    corr: pd.DataFrame = compute_spearman_corr(df)

    plt.figure(figsize=(12, 10))
    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        annot_kws={"size": 7},  # números más pequeños
        cmap="coolwarm",
        square=True,
        cbar_kws={"shrink": 0.8},
    )

    plt.title("Matriz de correlación (Spearman)", fontsize=12)

    # Evita solapamiento de etiquetas
    plt.xticks(rotation=45, ha="right", fontsize=8)
    plt.yticks(rotation=0, fontsize=8)

    # Ajuste automático de márgenes
    plt.tight_layout()

    if show:
        plt.show()
    else:
        plt.close()

