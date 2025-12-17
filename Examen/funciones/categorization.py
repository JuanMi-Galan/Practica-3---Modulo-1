from __future__ import annotations
import pandas as pd


def clasificar_columnas_continuas_discretas(df: pd.DataFrame) -> dict[str, list[str]]:
    """Clasifica las columnas del DataFrame según su tipo y cardinalidad.

    Definiciones:
        - Continuas:
            * Tipo numérico (int o float)
            * Más de 10 valores únicos
        - Discretas:
            * Diez o menos valores únicos
        - Alta cardinalidad:
            * Tipo no numérico (object, string, category)
            * Más de 10 valores únicos

    Args:
        df: DataFrame de entrada.

    Returns:
        dict[str, list[str]]: Diccionario con claves:
            - "continuas": columnas numéricas con >10 valores únicos
            - "discretas": columnas con <=10 valores únicos
            - "alta_cardinalidad": columnas no numéricas con >10 valores únicos
    """
    continuas: list[str] = []
    discretas: list[str] = []
    alta_cardinalidad: list[str] = []

    for col in df.columns:
        uniques = df[col].dropna().nunique()
        col_dtype = df[col].dtype

        # ***
        # Reglas
        # ***

        # 1. Discretas (<= 10 únicos)
        if uniques <= 10:
            discretas.append(col)
            continue

        # 2. Continuas (>10 únicos y tipo numérico)
        if pd.api.types.is_numeric_dtype(col_dtype) and uniques > 10:
            continuas.append(col)
            continue

        # 3. Alta cardinalidad (no numéricas y >10 únicos)
        alta_cardinalidad.append(col)

    return {
        "continuas": continuas,
        "discretas": discretas,
        "alta_cardinalidad": alta_cardinalidad,
    }
