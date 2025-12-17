"""
Paquete funciones - Módulo de utilidades para análisis de datos del examen.

Este paquete contiene funciones para:
- Funciones generales utiles
- Categorización de variables
- Preprocesamiento de datos
- Reducción de dimensionalidad
- Visualizaciones (heatmaps, histogramas, boxplots)
"""

# Importar funciones de categorización
from .categorization import clasificar_columnas_continuas_discretas

# Importar funciones de preprocesamiento
from .preprocessing import (
    completitud_datos,
    check_data_completeness,
    columnas_float_enteras
)

# Importar funciones de utils
from .utils import (
    detect_outliers,
    categorize_price,
    _plot_outliers,
    ambience_match,
    clean_null_strings,
)

# Importar funciones de reducción de dimensionalidad
from .dimension.poder_predictivo import poder_predictivo
from .dimension.transformacion_entropica import calcular_woe_iv

# Importar funciones de visualización
from .plots.heatmap import compute_spearman_corr, plot_heatmap
from .plots.histograms import plot_histograms
from .plots.boxplots import plot_boxplots

# Definir qué se exporta cuando se hace "from funciones import *"
__all__ = [
    # Categorización
    'clasificar_columnas_continuas_discretas',
    
    # Preprocesamiento
    'completitud_datos',
    'check_data_completeness',
    'columnas_float_enteras',
    
    # Reducción de dimensionalidad
    'poder_predictivo',
    'calcular_woe_iv',
    
    # Visualización
    'compute_spearman_corr',
    'plot_heatmap',
    'plot_histograms',
    'plot_boxplots',

    # Utils
    'detect_outliers',
    'categorize_price',
    '_plot_outliers',
    'ambience_match',
    'clean_null_strings',
]
