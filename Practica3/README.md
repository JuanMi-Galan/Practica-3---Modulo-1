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
6. [Instalación](#instalación)
7. [Test](#test)
8. [Uso](#uso)
9. [Ejemplos](#ejemplos)
11. [Licencia](#licencia)

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


## Instalación

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





## Deteccion de outliers

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

