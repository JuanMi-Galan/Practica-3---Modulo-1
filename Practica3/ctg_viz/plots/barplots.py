from typing import List

import matplotlib.pyplot as plt
import pandas as pd


def plot_barplots(df: pd.DataFrame, show: bool = True) -> None:
    """Genera barras horizontales ordenadas por frecuencia para variables categóricas.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    show : bool, optional
        Si True, muestra las figuras; si False, las cierra.

    Returns
    -------
    None
    """
    candidate_cols: List[str] = df.columns.tolist()
    cat_cols: List[str] = [c for c in candidate_cols if c in df.columns]

    for col in cat_cols:
        counts = df[col].value_counts().sort_values(ascending=True)

        plt.figure(figsize=(6, 4))
        plt.barh(counts.index.astype(str), counts.values)
        plt.title(f"Frecuencia de {col}")
        plt.xlabel("Frecuencia")

        if show:
            plt.show()
        else:
            plt.close()

    return None
