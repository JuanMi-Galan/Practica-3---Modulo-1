import pandas as pd
import numpy as np

def calcular_woe_iv(df: pd.DataFrame, variable: str, target: str):
    """
    Calcula WoE e IV para una variable categórica o binneada.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame con los datos.
    variable : str
        Nombre de la columna a evaluar (categórica o de bins).
    target : str
        Nombre de la columna objetivo binaria (0 = bueno, 1 = malo).

    Returns
    -------
    tabla_woe : pd.DataFrame
        Tabla con:
        - total, buenos, malos
        - dist_buenos, dist_malos
        - WoE, IV_bin (aporte al IV)
    iv_total : float
        Information Value total de la variable.
    """

    # Tabla de conteos por categoría/bin
    tabla = df.groupby(variable)[target].agg(['count', 'sum'])
    tabla.columns = ['total', 'malos']

    # Buenos = total - malos
    tabla['buenos'] = tabla['total'] - tabla['malos']

    # Totales globales
    total_buenos = tabla['buenos'].sum()
    total_malos  = tabla['malos'].sum()

    # Para evitar divisiones por cero
    eps = 1e-6

    # Distribuciones
    tabla['dist_buenos'] = tabla['buenos'] / (total_buenos + eps)
    tabla['dist_malos']  = tabla['malos']  / (total_malos  + eps)

    # WoE
    tabla['WoE'] = np.log((tabla['dist_buenos'] + eps) / (tabla['dist_malos'] + eps))

    # IV por categoría/bin
    tabla['IV_bin'] = (tabla['dist_buenos'] - tabla['dist_malos']) * tabla['WoE']

    # IV total
    iv_total = tabla['IV_bin'].sum()

    return tabla, iv_total