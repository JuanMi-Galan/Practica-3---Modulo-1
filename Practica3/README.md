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
5. [Instalación](#instalación)
6. [Uso](#uso)
7. [Estructura del Proyecto](#estructura-del-proyecto)
8. [Ejemplos](#ejemplos)
9. [Pruebas](#pruebas)
10. [Contribución](#contribución)
11. [Licencia](#licencia)

## Descripción

Este proyecto permite realizar ___, utilizando ___ como herramientas principales.

Incluye módulos para:
- Limpieza de datos
- Transformaciones
- Generación de reportes
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
- pytes
- matplotlib
- scipy
- typing
- scikit-learn
- seaborn

## Instalación

```bash
git clone https://github.com/usuario/proyecto.git
cd proyecto
pip install -r requirements.txt
```

## Test

Para la ejecución del test ejecutar:

```bash
py -m pytest ./Practica3/utils.py
```
Para ver detalles:

```bash
py -m pytest -vv ./Practica3/utils.py
```
Para ver solo si todo paso correctamente
```bash
pytest -q ./Practica3/utils.py
```

## Deteccion de outliers

Hacemos deteccion de outliers para las variables continuas, y para las discretas no ya que al tener pocos valores la deteccion de outliers con pocar variables categoricas nos puede eliminar valores comunes (al tener clases mayoritarias)

El proceso de eliminiacion va de variable en variable, eliminando iterativamente con los outliers que se detactan en cada variable anterior.

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