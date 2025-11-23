from typing import List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_histograms(df: pd.DataFrame, target_col: str = "NSP", show: bool = True) -> None:
    """Genera histogramas con KDE para todas las columnas numéricas."""
    
    sns.set(style="whitegrid")
    numeric_cols: List[str] = df.select_dtypes(include=["number"]).columns.tolist()
    has_target: bool = target_col in df.columns

    for col in numeric_cols:
        plt.figure(figsize=(6, 4))
        
        # Evitar KDE cuando la varianza es 0
        use_kde = df[col].var() > 0

        if has_target:
            sns.histplot(
                data=df,
                x=col,
                hue=target_col,
                kde=use_kde,
                element="step",
                stat="density",
                common_norm=False,
            )
        else:
            sns.histplot(
                data=df,
                x=col,
                kde=use_kde,
                stat="density",
            )

        plt.title(f"Histograma de {col}")

        if show:
            plt.show()
        else:
            plt.close()

    return None
