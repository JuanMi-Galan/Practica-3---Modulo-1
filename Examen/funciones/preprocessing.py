# Defini la funcion para ver la completitud de los datos
from __future__ import annotations
import pandas as pd
from typing import Dict, List


def completitud_datos(df: pd.DataFrame) -> pd.Series:
    """Calcula el porcentaje de valores nulos por columna.

    Esta función recibe un DataFrame de pandas y devuelve, para cada columna,
    el porcentaje de valores nulos, ordenado de mayor a menor.

    Args:
        df: DataFrame de entrada.

    Returns:
        pd.Series: Serie con el porcentaje de valores nulos por columna,
        redondeado a 2 decimales y ordenado de mayor a menor.
    """
    if df.empty:
        return pd.Series(dtype="float64")

    porcentaje_nulos = df.isna().sum().sort_values(ascending=False) / len(df) * 100
    return porcentaje_nulos.round(2)

def check_data_completeness(df: pd.DataFrame) -> pd.DataFrame:
    """Resume la completitud y estadísticos de dispersión por columna.

    Para cada columna del DataFrame calcula:
      - Conteo de valores nulos.
      - Porcentaje de completitud (valores no nulos).
      - Tipo de dato.
      - Estadísticos de dispersión (solo para columnas numéricas):
        media, desviación estándar, mínimo, cuartil 1, mediana,
        cuartil 3 y máximo.

    Args:
        df: DataFrame de entrada.

    Returns:
        pd.DataFrame: DataFrame con índice igual al nombre de las columnas
        originales y las columnas:
        - ``n_nulls``: número de valores nulos.
        - ``pct_completeness``: porcentaje de valores no nulos (0–100), redondeado a 2 decimales.
        - ``dtype``: tipo de dato de la columna.
        - ``mean``, ``std``, ``min``, ``q1``, ``median``, ``q3``, ``max``:
          estadísticos de dispersión para columnas numéricas, ``NaN`` para el resto.
    """
    # Si el DataFrame no tiene filas, devolvemos estructura vacía
    if df.empty:
        return pd.DataFrame(
            columns=[
                "Num_nulls",
                "%_completeness",
                "dtype",
                "mean",
                "std",
                "min",
                "25%",
                "50%",
                "75%",
                "max",
            ]
        )

    # Porcentaje de completitud (no-nulos)
    pct_completeness: pd.Series = (1 - df.isna().sum() / len(df)) * 100

    # Tipos de dato
    dtypes: pd.Series = df.dtypes.astype(str)

    # Base del resumen
    resumen = pd.DataFrame(
        {
            "Num_nulls": df.isna().sum(),
            "%_completeness": pct_completeness.round(2),
            "dtype": dtypes,
        }
    )

    # Estadísticos de dispersión solo para columnas numéricas
    # describe() ya ignora las columnas no numéricas
    numeric_stats = df.describe().T[
        ["mean", "std", "min", "25%", "50%", "75%", "max"]
    ]

    # Hacemos join para tener todo junto
    resumen = resumen.join(numeric_stats, how="left")

    return resumen

def columnas_float_enteras(df: pd.DataFrame) -> Dict[str, List[str]]:
    """Clasifica columnas float en enteras o decimales.

    Args:
        df (pd.DataFrame): DataFrame de entrada.

    Returns:
        Dict[str, List[str]]:
            - "enteras": columnas cuyos valores float no nulos son enteros.
            - "decimales": columnas float con algún valor decimal.
    """
    float_cols = df.select_dtypes(include=["float", "float64"]).columns

    enteras = [
        col for col in float_cols
        if (df[col].dropna() % 1 == 0).all()
    ]

    decimales = [col for col in float_cols if col not in enteras]

    return {"enteras": enteras, "decimales": decimales}