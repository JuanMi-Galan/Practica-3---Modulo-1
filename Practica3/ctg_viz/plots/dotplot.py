from typing import List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_dotplots(
    df: pd.DataFrame,
    target_col: str = "NSP",
    show: bool = True,
) -> None:
    """Genera dot plots (stripplots) para todas las columnas numéricas.

    Compara la distribución entre los dos grupos más frecuentes de la
    columna objetivo (overlay de puntos).

    Args:
        df: DataFrame de entrada.
        target_col: Columna objetivo para definir los grupos.
        show: Si es True se muestran las figuras; si es False se cierran.

    Returns:
        None
    """
    sns.set(style="whitegrid")

    if target_col not in df.columns:
        # Si no existe la columna objetivo, no se generan gráficos.
        return None

    numeric_cols: List[str] = df.select_dtypes(include=["number"]).columns.tolist()

    # Tomar solo 2 grupos más frecuentes
    value_counts = df[target_col].value_counts()
    if value_counts.shape[0] < 2:
        # No hay suficientes grupos para comparación
        return None

    top_groups = value_counts.index[:2]
    mask = df[target_col].isin(top_groups)
    df_two_groups = df.loc[mask, :]

    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(6, 4))

        sns.stripplot(
            data=df_two_groups,
            x=target_col,
            y=col,
            dodge=True,
            jitter=True,
            alpha=0.7,
            ax=ax,
        )

        ax.set_title(f"Dot plot de {col} para 2 grupos de {target_col}")
        ax.set_xlabel(target_col)
        ax.set_ylabel(col)

        fig.tight_layout()

        if show:
            plt.show()
        else:
            plt.close(fig)

    return None
