from typing import List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_density(df: pd.DataFrame, target_col: str = "NSP", show: bool = True) -> None:
    """Genera curvas de densidad (KDE) para todas las columnas numéricas.
    
    Si existe la columna objetivo, se traza una densidad por clase, siempre
    evitando generar KDE cuando la varianza es cero.

    Parámetros
    ----------
    df : pandas.DataFrame
        DataFrame de entrada.
    target_col : str, optional
        Columna objetivo para colorear las densidades.
    show : bool, optional
        Si True muestra las figuras; si False las cierra.
    """
    sns.set(style="whitegrid")

    numeric_cols: List[str] = df.select_dtypes(include=["number"]).columns.tolist()
    has_target: bool = target_col in df.columns

    for col in numeric_cols:
        plt.figure(figsize=(6, 4))

        # Verificar varianza
        if df[col].nunique() <= 1 or df[col].var() == 0:
            # Caso varianza cero → KDE no es posible
            plt.axvline(df[col].iloc[0], color="blue", linestyle="--")
            plt.title(f"{col}: Varianza cero (valor único = {df[col].iloc[0]})")
            
            if show:
                plt.show()
            else:
                plt.close()
            continue  # Saltar al siguiente col

        # Si tiene varianza > 0, sí graficamos KDE
        if has_target:
            sns.kdeplot(
                data=df,
                x=col,
                hue=target_col,
                fill=True,
                common_norm=False,
                alpha=0.4,
                warn_singular=False
            )
            plt.title(f"Densidad de {col} por {target_col}")
        else:
            sns.kdeplot(df[col], fill=True)
            plt.title(f"Densidad de {col}")

        if show:
            plt.show()
        else:
            plt.close()

    return None
