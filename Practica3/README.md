# Practica 3 - Análisis Exploratorio con Visualizaciones y Librería Personalizada

Fecha:
22/11/2025

Descripción:
Este proyecto tratara la data que contiene valores nulos, 

Integrante:
- Juan Miguel Galan Olivares

## Tabla de Contenido
1. [Descripción](#descripción)
2. [Diccionario de datos](#diccionario-de-datos)
3. [Características](#características)
4. [Requisitos](#requisitos)
5. [Estructura del Proyecto](#estructura-del-proyecto)
6. [Clonación del proyecto](#clonación-del-proyecto)
7. [Test](#test)
8. [Uso](#uso)
10. [Consideraciones](#consideraciones)
11. [Ejemplos](#ejemplos)
12. [Licencia](#licencia)

## Descripción

Este proyecto permite realizar analisis exploratorio, manejo de valores ausentes y extremos, utilizando funciones de python y funciones propias como herramientas principales.

Incluye módulos para:
- Limpieza de datos
- Modelado y validación

## Diccionario de datos

### Información del examen
| Columna | Descripción |
|--------|-------------|
| **FileName** | Nombre del archivo del examen |
| **Date** | Fecha del examen |
| **b** | Instante de inicio |
| **e** | Instante de término |

### Medidas de variabilidad (SisPorto)
| Columna | Descripción |
|--------|-------------|
| **LBE** | Línea base (médico) |
| **LB** | Línea base (SisPorto) |
| **AC** | Aceleraciones |
| **FM** | Movimientos fetales |
| **UC** | Contracciones uterinas |
| **ASTV** | % variabilidad anormal corto plazo |
| **MSTV** | Media corto plazo |
| **ALTV** | % variabilidad anormal largo plazo |
| **MLTV** | Media largo plazo |

### Desaceleraciones
| Columna | Descripción |
|--------|-------------|
| **DL** | Leves |
| **DS** | Severas |
| **DP** | Prolongadas |
| **DR** | Repetitivas |

### Histogramas
| Columna | Descripción |
|--------|-------------|
| **Width** | Ancho |
| **Min** | Mínimo |
| **Max** | Máximo |
| **Nmax** | Picos |
| **Nzeros** | Ceros |
| **Mode** | Moda |
| **Mean** | Media |
| **Median** | Mediana |
| **Variance** | Varianza |
| **Tendency** | Tendencia (-1=Asimetria a la izquierda; 0=Simetrica; 1=Asimetria a la derecha) |

### Patrones fisiológicos
| Columna | Descripción |
|--------|-------------|
| **A** | Sueño calmo |
| **B** | Sueño REM |
| **C** | Vigilia calmada |
| **D** | Vigilia activa |
| **AD** | Acelerativo/desacelerativo |
| **DE** | Desacelerativo |
| **LD** | Largamente desacelerativo |
| **FS** | Plano-sinusoidal |
| **SUSP** | Sospechoso |

### Diagnóstico
| Columna | Descripción |
|--------|-------------|
| **CLASS** | Clase (1–10) |
| **NSP** | Estado fetal (1=Normal, 2=Sospechoso, 3=Patológico) |

## Características

- Procesamiento masivo de datos
- Validaciones automáticas
- Integración con API externa
- Exportación a Excel/SQL
- Pruebas con pytest

## Requisitos
Para la optención de las librerias del entorno virtual se ejecuto:
```bash
pip freeze > ./Practica3/requirements.txt
```
En linux sin las versiones y se movio dentro de la carpeta Practica3:
```bash
pip freeze | sed -E 's/==.*//' > ./Practica3requirements.txt
```

- Python 3.9+
- pip
- Git
- pandas
- pytest
- matplotlib
- scipy
- typing
- scikit-learn
- seaborn

## Estructura del Proyecto
La carpeta de la practica3 se encuentra dentro de la carpeta PRACTICAS, donde se creo un entorno virtual con las librerias mencionadas anteriormente.

```text
PRACTICAS
📦 Practica3
 ┣ 📂 ctg_viz
 ┃ ┣ 📂 plots
 ┃ ┃ ┣ 📝 barplots.py
 ┃ ┃ ┣ 📝 boxplots.py
 ┃ ┃ ┣ 📝 density.py
 ┃ ┃ ┣ 📝 dotplot.py
 ┃ ┃ ┣ 📝 heatmap.py
 ┃ ┃ ┣ 📝 histograms.py
 ┃ ┃ ┣ 📝 lineas.py
 ┃ ┃ ┗ 📝 violin.py
 ┃ ┣ 📝 __init__.py
 ┃ ┣ 📝 categorization.py
 ┃ ┗ 📝 preprocessing.py
 ┣ 📂 data
 ┃ ┗ 📝 CTG.csv
 ┣ 📝 Practica3.ipynb
 ┣ 📝 README.md
 ┣ 📝 gitignore.txt
 ┣ 📝 requirements.txt
 ┗ 📝 utils.py
LICENSE
```


## Clonación del proyecto

```bash
git clone https://github.com/JuanMi-Galan/Practica-3---Modulo-1.git
```

## Test

Para la ejecución del test ejecutar:

```bash
pytest ./Practica3/utils.py
```
Para ver detalles:

```bash
pytest -vv ./Practica3/utils.py
```
Para ver solo si todo paso correctamente
```bash
pytest -q ./Practica3/utils.py
```
## Uso
Se descraga la data de: https://www.kaggle.com/code/akshat0007/cardiotocology/data, esta se pondra dentro de la carpeta Practica3/data con el nombre de `CTG.csv`. Para posteriormente solo ejecutar el archivo `Practica3.ipynb`, el cual solo se tendria que modificar el nombre del archivo si es que no se modifico a `CTG.csv`.

En el archivo `Practica3.ipynb` se puede ver el claro ejemplo de como funciona cada una de las funciones.

### Descripción de Funciones Utilizadas

**Funciones de Preprocesamiento:**

- **`completitud_datos(data)`**: Analiza el porcentaje de valores faltantes por columna, ordenando de mayor a menor. Retorna un DataFrame con el conteo y porcentaje de valores nulos.

- **`check_data_completeness_juan_miguel_galan_olivares(data)`**: Verifica la completitud general del dataset proporcionando estadísticas de valores nulos totales y por columna.

- **`columnas_float_enteras(data)`**: Identifica y clasifica columnas numéricas según si contienen decimales o son valores enteros, facilitando la selección de estrategias de imputación.

- **`SimpleImputer(strategy)`**: Imputa valores faltantes usando estrategias simples:
  - `'most_frequent'`: Para variables categóricas (moda)
  - `'median'`: Para variables numéricas enteras
  - `'mean'`: Para variables con decimales

- **`KNNImputer(n_neighbors)`**: Imputa valores basándose en los k vecinos más cercanos. Útil para variables interdependientes donde el contexto importa.

**Funciones de Análisis:**

- **`detect_outliers(data, methods, z_threshold, iqr_factor, plot, return_details)`**: Detecta valores atípicos usando:
  - **IQR (Rango Intercuartílico)**: Identifica valores fuera de Q1-1.5*IQR y Q3+1.5*IQR
  - **Z-score**: Detecta valores con |z| > threshold (típicamente 3)
  - Retorna índices de outliers y permite visualización

- **`clasificar_columnas_continuas_discretas(data)`**: Clasifica automáticamente las columnas en:
  - **Continuas**: >10 valores únicos y tipo numérico
  - **Discretas**: ≤10 valores únicos
  - **Alta cardinalidad**: Muchos valores únicos (categóricas textuales)

**Funciones de Visualización Estática (Matplotlib/Seaborn):**

- **`plot_histograms(data, target_col)`**: Genera histogramas para distribuciones de variables continuas, con opción de segmentación por variable objetivo.

- **`plot_boxplots(data, target_col)`**: Crea diagramas de caja para identificar outliers y comparar distribuciones entre grupos.

- **`plot_barplots(data)`**: Visualiza frecuencias de variables discretas mediante gráficos de barras horizontales.

- **`plot_density(data, target_col)`**: Grafica curvas de densidad de probabilidad para visualizar distribuciones suavizadas.

- **`plot_heatmap(data, method)`**: Genera mapas de calor de correlaciones (Pearson, Spearman) entre variables numéricas.

- **`plot_violins(data, target_col)`**: Combina boxplots con densidad (violin) y swarmplot para visualizaciones detalladas de distribuciones.

- **`plot_lineplots(data, time_col)`**: Muestra tendencias temporales o secuenciales de variables continuas.

- **`plot_dotplots(data, target_col)`**: Representa distribuciones mediante puntos, útil para comparar grupos categóricos.

## Consideraciones

Hacemos deteccion de outliers para las variables continuas, y para las discretas no ya que al tener pocos valores la deteccion de outliers con pocar variables categoricas nos puede eliminar valores comunes (al tener clases mayoritarias)

El proceso de eliminiacion va de variable en variable, eliminando iterativamente con los outliers que se detactan en cada variable anterior.

En total eliminamos el 20% aproximadamente del conjunto total, esto para tener una mejor visualización de nuestros datos. Ya que al ser datos medicos la mejor ocpion para detectar outliers es tener los parametros en los que una persona viva no puede tener, mediante una investigación.

Nosotros utilizamos IQR y Z-score eliminando los datos que coicidieran en ambos como outliers. Teniendo el siguiente resultado.

Para la variable AC
- Se detectaron 35 valores

Para la variable FM
- Se detectaron 31 valores

Para la variable UC
- Se detectaron 12 valores

Para la variable MSTV
- Se detectaron 31 valores

Para la variable ALTV
- Se detectaron 57 valores

Para la variable MLTV
- Se detectaron 29 valores

Para la variable DL
- Se detectaron 24 valores

Para la variable Max
- Se detectaron 11 valores

Para la variable Nmax
- Se detectaron 11 valores

Para la variable Mode
- Se detectaron 36 valores

Para la variable Mean
- Se detectaron 17 valores

Para la variable Median
- Se detectaron 2 valores

Para la variable Variance
- Se detectaron 48 valores

## Ejemplos


## Licencia
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Este proyecto está disponible bajo la licencia MIT.  
Consulta el archivo [LICENSE](LICENSE) para más detalles.
