from typing import List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_violins(
    df: pd.DataFrame,
    target_col: str = "NSP",
    show: bool = True,
) -> None:
    """Genera gráficos de violín con overlay de swarmplot o stripplot.

    Si hay demasiados puntos, usa stripplot automáticamente para evitar warnings.
    """

    sns.set(style="whitegrid")

    if target_col not in df.columns:
        return None

    numeric_cols: List[str] = df.select_dtypes(include=["number"]).columns.tolist()

    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(6, 4))

        # Violín
        sns.violinplot(
            data=df,
            x=target_col,
            y=col,
            inner="quartile",
            ax=ax,
        )

        # Determinar si hay demasiados puntos
        n_points = df[col].count()
        use_strip = n_points > 300  # umbral recomendado

        if use_strip:
            sns.stripplot(
                data=df,
                x=target_col,
                y=col,
                color="k",
                alpha=0.4,
                size=1,
                jitter=0.2,
                ax=ax,
            )
        else:
            sns.swarmplot(
                data=df,
                x=target_col,
                y=col,
                color="k",
                alpha=0.5,
                size=1,  # reducido para evitar warnings
                ax=ax,
            )

        ax.set_title(f"Violin + {'stripplot' if use_strip else 'swarmplot'} de {col} por {target_col}")
        ax.set_xlabel(target_col)
        ax.set_ylabel(col)

        fig.tight_layout()

        if show:
            plt.show()
        else:
            plt.close(fig)

    return None

