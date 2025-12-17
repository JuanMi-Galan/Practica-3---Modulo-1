# Análisis Predictivo de Calificaciones de Restaurantes

## Entregables
• [.ipynb] Código utilizado para la construcción de la solución.

Link: https://github.com/JuanMi-Galan/Practica-3---Modulo-1/blob/351518be40c0f939d8b7ea18158caeed6f36ab39/Examen/Examen.ipynb

• [.png] Imagenes del conjunto de datos reducido con PCA.

Link: https://github.com/JuanMi-Galan/Practica-3---Modulo-1/blob/351518be40c0f939d8b7ea18158caeed6f36ab39/Examen/datos/PCA.png

• [.csv] Tablas analíticas de datos identificadas como restaurantes.csv y 
usuarios.csv. 

Links: 
- https://github.com/JuanMi-Galan/Practica-3---Modulo-1/blob/351518be40c0f939d8b7ea18158caeed6f36ab39/Examen/datos/data_analitica_con_nulos_y_outliers.csv

- https://github.com/JuanMi-Galan/Practica-3---Modulo-1/blob/351518be40c0f939d8b7ea18158caeed6f36ab39/Examen/datos/data_analitica_sin_nulos_ni_outliers.csv

• [url/.pdf] Tablero dinámico funcional. Esto solo en caso de haber realizado tablero. 

Link: https://public.tableau.com/views/Restaurantes-Clientes/Restaurantes-Clientes?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

• [.pdf] Elaboración de un documento entregando todos los puntos. Este README.md en pdf.

Link: https://github.com/JuanMi-Galan/Practica-3---Modulo-1/blob/351518be40c0f939d8b7ea18158caeed6f36ab39/Examen/README.md

### Adicionales

• [.link/.pdf] Grafica del modelo entidad de los datos utilizados, para su contextualización.

Link: https://miro.com/app/board/uXjVGfOj0JE=/?share_link_id=7282565746

### Cuestionario 
• (0.5 puntos) ¿Por qué Excel no es una Base de Datos? Elabore.

Excel no es una base de datos porque no garantiza integridad, seguridad ni concurrencia de usuarios. Además, no está diseñado para manejar grandes volúmenes de información ni transacciones de forma eficiente.

En cambio, una base de datos está diseñada para almacenar, consultar y proteger grandes volúmenes de información de manera eficiente, consistente y escalable.

• (0.5 puntos) ¿Qué diferencia hay entre un Ingeniero de Datos, un Científico de Datos y un Arquitecto de Datos? 

El Ingeniero de Datos construye y mantiene los flujos de datos, asegurando que la información llegue limpia, estructurada y disponible desde las fuentes hasta los sistemas analíticos; el Científico de Datos analiza y modela para generar predicciones,aplicando estadística, machine learning y conocimiento del negocio; y el Arquitecto de Datos diseña la estructura y estrategia del sistema de datos, definiendo cómo se almacenan, integran y gobiernan los datos a nivel organizacional.

• (0.5 puntos) ¿Cómo reduce dimensiones PCA? 

PCA reduce dimensiones transformando variables correlacionadas en componentes principales no correlacionadas que conservan la mayor varianza con menos variables.

Estas componentes son combinaciones lineales de las variables originales y se ordenan según la cantidad de varianza que explican.

• (0.5 puntos) ¿Cuál es la diferencia entre importancia de variables y poder predictivo? 

La importancia de variables indica qué tan relevante es una variable dentro de un modelo específico, por ejemplo, cuánto contribuye a una predicción en un árbol o modelo de machine learning.

El poder predictivo, en cambio, mide qué tan bien una variable puede discriminar o predecir el resultado por sí misma, independientemente del modelo, usando métricas como IV, AUC o correlación con la variable objetivo.

Una variable puede tener alta importancia en un modelo por interacción con otras, pero bajo poder predictivo individual, y viceversa.

### Feedback
(0 puntos) Por favor, aporte comentarios sobre el avance del curso, el ponente y las clases. El objetivo es poder mejorar los contenidos y el desarrollo del diplomado. 

Los temas contemplados en el módulo sí se revisaron de acuerdo con el programa. Sin embargo, me hubiera gustado que se profundizara un poco más en cómo aplicar estos conceptos en distintos contextos, dedicando más tiempo a la explicación y al análisis de los temas antes de pasar directamente a la práctica. En algunos casos, la práctica consumió la mayor parte del tiempo del módulo, por lo que considero que un mayor énfasis en la parte conceptual y su aplicación gradual habría enriquecido el aprendizaje.

## Descripción del Proyecto

### Contexto de Negocio

Este proyecto analiza el comportamiento de usuarios al calificar restaurantes, con el objetivo de identificar los factores clave que influyen en las calificaciones otorgadas. El análisis permite:

- **Mejorar la experiencia del cliente**: Identificando qué aspectos del servicio, ambiente y características del restaurante impactan más en la satisfacción.
- **Optimizar estrategias de marketing**: Segmentando usuarios según preferencias y comportamientos.
- **Tomar decisiones informadas**: Ayudando a restaurantes a enfocar recursos en áreas que realmente importan a sus clientes.
- **Predecir satisfacción**: Desarrollando modelos que anticipen calificaciones basándose en características del usuario y del establecimiento.

### Objetivo Técnico

Realizar un análisis exploratorio completo del dataset de calificaciones de restaurantes aplicando técnicas avanzadas de ciencia de datos:

1. **Ingeniería de características**: Creación de variables derivadas que capturen patrones ocultos
2. **Limpieza y preprocesamiento**: Manejo de valores faltantes, outliers y normalización
3. **Reducción de dimensionalidad**: Aplicación de PCA y clustering de variables
4. **Selección de variables**: Identificación de predictores clave mediante métodos estadísticos y de información

### Unidad Muestral

**Ratings**: Cada fila representa una calificación que un usuario otorga a un restaurante, enriquecida con características del usuario y del establecimiento.

La unidad muestral permite la unión de información de usuarios y restaurantes, facilitando:
- Análisis del comportamiento del usuario y características del restaurante
- Generación de variables derivadas para modelos de recomendación y satisfacción
- Utilización de la calificación como variable objetivo

---

## Estructura del Proyecto

```
📦Examen
 ┣ 📂datos # Datasets originales
 ┃ ┣ 📜cuisine.csv
 ┃ ┣ 📜data_analitica_con_nulos_y_outliers.csv # Data analitica
 ┃ ┣ 📜data_analitica_sin_nulos_ni_outliers.csv # Data analitica para modelar
 ┃ ┣ 📜hours.csv
 ┃ ┣ 📜parking.csv
 ┃ ┣ 📜payment_methods.csv
 ┃ ┣ 📜PCA.png
 ┃ ┣ 📜ratings.csv
 ┃ ┣ 📜restaurants.csv
 ┃ ┣ 📜restaurants.xlsx
 ┃ ┣ 📜usercuisine.csv
 ┃ ┣ 📜userpayment.csv
 ┃ ┣ 📜users.csv
 ┃ ┗ 📜users.xlsx
 ┣ 📂funciones # Módulos personalizados
 ┃ ┣ 📂dimension  # Reducción de dimensionalidad
 ┃ ┃ ┣ 📜multicolinealidad.py
 ┃ ┃ ┣ 📜poder_predictivo.py
 ┃ ┃ ┣ 📜reduccion_dimension.py
 ┃ ┃ ┗ 📜transformacion_entropica.py
 ┃ ┣ 📂plots  # Visualizaciones
 ┃ ┃ ┣ 📜boxplots.py
 ┃ ┃ ┣ 📜heatmap.py
 ┃ ┃ ┗ 📜histograms.py
 ┃ ┣ 📜categorization.py
 ┃ ┣ 📜preprocessing.py
 ┃ ┣ 📜utils.py
 ┃ ┗ 📜__init__.py
 ┣ 📜.gitignore
 ┣ 📜datos-20240720T141705Z-001.zip  # Datasets originales en zip
 ┣ 📜Examen.ipynb  # Notebook principal con análisis completo
 ┣ 📜README.md
 ┗ 📜requirements.txt  # Dependencias del proyecto
```

---

## Instalación y Configuración

### Requisitos Previos

- Python 3.13.5
- Jupyter Notebook

### Instalación

```bash
# Clonar el repositorio (se encuentra en la carpeta Examen)
https://github.com/JuanMi-Galan/Practica-3---Modulo-1.git

git@github.com:JuanMi-Galan/Practica-3---Modulo-1.git

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar Jupyter Notebook
jupyter notebook Examen.ipynb
```

---

## Documentación de Módulos

### Módulo: `funciones`

Paquete personalizado que contiene todas las funciones de análisis desarrolladas durante el diplomado.

#### Importación Simplificada

```python
from funciones import *
```

---

### `preprocessing.py` - Preprocesamiento de Datos

#### `completitud_datos(df: pd.DataFrame) -> pd.Series`

**Propósito**: Evalúa la calidad de los datos calculando el porcentaje de valores faltantes por columna.

**Uso de Negocio**: Identifica rápidamente qué variables requieren atención inmediata antes de cualquier análisis.

**Parámetros**:
- `df`: DataFrame de entrada

**Retorna**:
- Serie con porcentaje de nulos por columna (ordenado de mayor a menor)

**Ejemplo**:
```python
completitud_datos(df).head(10)
# Output:
# address         62.45
# zip             45.32
# smoking_area    23.10
# ...
```

---

#### `check_data_completeness(df: pd.DataFrame) -> pd.DataFrame`

**Propósito**: Proporciona un resumen completo de completitud y estadísticos descriptivos.

**Uso de Negocio**: Genera un reporte ejecutivo del estado de los datos, combinando análisis de calidad con estadísticas básicas.

**Parámetros**:
- `df`: DataFrame de entrada

**Retorna**:
- DataFrame con:
  - `Num_nulls`: Cantidad de valores faltantes
  - `%_completeness`: Porcentaje de completitud
  - `dtype`: Tipo de dato
  - Estadísticos: mean, std, min, 25%, 50%, 75%, max (solo numéricos)

**Ejemplo**:
```python
completeness_report = check_data_completeness(df)
```

**Interpretación**:
- Variables con <80% completitud: considerar eliminación o imputación estratégica
- Desviación estándar alta: posibles outliers o alta variabilidad en el negocio

---

#### `columnas_float_enteras(df: pd.DataFrame) -> Dict[str, List[str]]`

**Propósito**: Diferencia entre columnas numéricas que representan valores enteros vs decimales.

**Uso de Negocio**: Permite aplicar estrategias de imputación específicas (mediana para enteros, media para decimales).

**Parámetros**:
- `df`: DataFrame de entrada

**Retorna**:
- Diccionario con claves:
  - `"enteras"`: Columnas float que son números enteros
  - `"decimales"`: Columnas con decimales verdaderos

**Ejemplo**:
```python
clasificacion = columnas_float_enteras(df)
# {'enteras': ['age', 'num_visits'], 'decimales': ['price', 'rating']}
```

---

### `categorization.py` - Clasificación de Variables

#### `clasificar_columnas_continuas_discretas(df: pd.DataFrame) -> dict[str, list[str]]`

**Propósito**: Clasifica automáticamente las columnas según su naturaleza estadística.

**Uso de Negocio**: Fundamental para elegir el análisis correcto (correlación de Pearson vs Spearman, tests paramétricos vs no paramétricos).

**Criterios**:
- **Continuas**: Numéricas con >10 valores únicos
- **Discretas**: ≤10 valores únicos (incluye categóricas numéricas)
- **Alta cardinalidad**: No numéricas con >10 valores únicos

**Parámetros**:
- `df`: DataFrame de entrada

**Retorna**:
- Diccionario con claves:
  - `"continuas"`: Variables numéricas continuas
  - `"discretas"`: Variables discretas/categóricas
  - `"alta_cardinalidad"`: Variables categóricas con muchas categorías

**Ejemplo**:
```python
clasificacion = clasificar_columnas_continuas_discretas(df)

# Aplicar estrategias diferenciadas
for col in clasificacion['continuas']:
    # Análisis de distribución, outliers
    
for col in clasificacion['discretas']:
    # Tablas de frecuencia, gráficos de barras
    
for col in clasificacion['alta_cardinalidad']:
    # Considerar agrupación o eliminación
```

---

### `dimension/poder_predictivo.py` - Selección de Variables

#### `poder_predictivo(X: pd.DataFrame, y, num_k: int) -> tuple`

**Propósito**: Identifica las K variables con mayor poder predictivo usando estadística F (ANOVA).

**Uso de Negocio**: Reduce el modelo a las variables más importantes, mejorando interpretabilidad y reduciendo costo computacional.

**Parámetros**:
- `X`: DataFrame con variables explicativas
- `y`: Variable objetivo (categórica)
- `num_k`: Número de mejores variables a seleccionar

**Retorna**:
- `data_poder_predictivo`: DataFrame con las K variables seleccionadas (transformadas)
- `scores`: DataFrame con todas las variables y su score F
- `selected_features`: Array con nombres de variables seleccionadas
- `fig`: Gráfico interactivo de Plotly con los scores

**Características Técnicas**:
- Aplica **OneHotEncoder** automáticamente a variables categóricas
- Utiliza **SelectKBest** con función de score `f_classif`
- Maneja matrices dispersas (CSR) eficientemente

**Ejemplo**:
```python
X = df.drop(columns=['rating'])
y = df['rating']

data, scores, features, fig = poder_predictivo(X, y, num_k=5)

# Top 5 variables:
# 1. color_purple: 245.67
# 2. hijos_kids: 198.43
# 3. personality_hunter: 156.22
# ...

fig.show()  # Visualizar scores
```

**Interpretación de Scores**:
- Score >100: Variable altamente predictiva
- Score 50-100: Variable moderadamente relevante
- Score <50: Variable con bajo poder predictivo

---

### `dimension/transformacion_entropica.py` - WoE e IV

#### `calcular_woe_iv(df: pd.DataFrame, variable: str, target: str) -> tuple`

**Propósito**: Calcula Weight of Evidence (WoE) e Information Value (IV) para evaluar poder predictivo de variables categóricas.

**Uso de Negocio**: 
- Identifica qué categorías de una variable están asociadas con mayor/menor riesgo
- Cuantifica la importancia de la variable para predecir el evento objetivo
- Usado extensivamente en modelos de credit scoring y análisis de riesgo

**Parámetros**:
- `df`: DataFrame con los datos
- `variable`: Nombre de la columna categórica a evaluar
- `target`: Variable objetivo binaria (0 = negativo, 1 = positivo)

**Retorna**:
- `tabla_woe`: DataFrame con:
  - `total`, `buenos`, `malos`: Conteos por categoría
  - `dist_buenos`, `dist_malos`: Distribuciones
  - `WoE`: Weight of Evidence por categoría
  - `IV_bin`: Contribución al IV total
- `iv_total`: Information Value total de la variable

**Interpretación de WoE**:
- **WoE > 0**: Categoría asociada con menor riesgo (más "buenos")
- **WoE < 0**: Categoría asociada con mayor riesgo (más "malos")
- **WoE ≈ 0**: Categoría neutral

**Interpretación de IV**:
- **IV < 0.02**: Variable sin poder predictivo
- **IV 0.02-0.10**: Poder predictivo débil
- **IV 0.10-0.30**: Poder predictivo medio
- **IV 0.30-0.50**: Poder predictivo fuerte
- **IV > 0.50**: Poder predictivo muy fuerte (posible sobreajuste)

**Ejemplo**:
```python
tabla, iv = calcular_woe_iv(df, variable='color', target='rating')

print(f'IV total: {iv:.2f}')
# IV total: 4.66 (Extraordinaria)

display(tabla)
#              total  buenos  malos  dist_buenos  dist_malos    WoE  IV_bin
# purple        450    320     130        0.42        0.18    0.85   0.20
# red           300    150     150        0.20        0.21   -0.05   0.00
# yellow        200     80     120        0.11        0.17   -0.43   0.03
```

**Aplicación en Negocio**:
```python
# Evaluar todas las variables categóricas
for var in variables_categoricas:
    tabla, iv = calcular_woe_iv(df, variable=var, target='rating_alto')
    if iv > 0.30:
        print(f"{var}: IV={iv:.2f} - INCLUIR en modelo")
```

---

### `plots/heatmap.py` - Visualización de Correlaciones

#### `compute_spearman_corr(df: pd.DataFrame) -> pd.DataFrame`

**Propósito**: Calcula la matriz de correlación de Spearman para variables numéricas.

**Uso de Negocio**: Spearman es robusto a outliers y captura relaciones monotónicas no lineales.

**Parámetros**:
- `df`: DataFrame de entrada

**Retorna**:
- Matriz de correlación de Spearman

---

#### `plot_heatmap(df: pd.DataFrame, show: bool = True) -> None`

**Propósito**: Visualiza la matriz de correlación con un mapa de calor.

**Uso de Negocio**: Identifica rápidamente multicolinealidad y relaciones entre variables.

**Parámetros**:
- `df`: DataFrame de entrada
- `show`: Si mostrar el gráfico inmediatamente

**Interpretación**:
- **Correlación ≈ 1 o -1**: Variables altamente correlacionadas (considerar eliminar una)
- **Correlación ≈ 0**: Variables independientes
- Colores cálidos (rojo): Correlación positiva
- Colores fríos (azul): Correlación negativa

**Ejemplo**:
```python
plot_heatmap(df)

# Acción basada en resultados:
# - latitude_user y age tienen correlación 1.0 -> Eliminar birth_year
# - longitude_user y longitude_rest correlación 0.85 -> Crear variable distancia
```

---

### `plots/histograms.py` y `plots/boxplots.py`

#### `plot_histograms(df: pd.DataFrame, target_col: str, show: bool = True) -> None`

**Propósito**: Genera histogramas de todas las variables numéricas segmentadas por la variable objetivo.

**Uso de Negocio**: Identifica si las distribuciones difieren entre clases (poder discriminante).

---

#### `plot_boxplots(df: pd.DataFrame, target_col: str, show: bool = True) -> None`

**Propósito**: Crea boxplots para comparar distribuciones entre categorías de la variable objetivo.

**Uso de Negocio**: 
- Detecta outliers por clase
- Identifica variables con diferente comportamiento entre grupos
- Valida hipótesis sobre factores diferenciadores

---

## Flujo de Análisis

### Ingeniería de Características

Se crearon 6 variables adicionales para enriquecer el análisis:

| Variable | Descripción | Justificación de Negocio |
|----------|-------------|--------------------------|
| `age` | Edad del usuario (2025 - birth_year) | La edad puede influir en preferencias gastronómicas |
| `dist_user_restaurant` | Distancia euclidiana entre usuario y restaurante | Usuarios pueden preferir lugares cercanos |
| `match_cuisine` | Coincidencia entre preferencia de usuario y cocina del restaurante | Alineación de expectativas con oferta |
| `restaurant_popularity` | Número de calificaciones recibidas | Popularidad puede influir en percepción |
| `rating_comida_service` | Promedio ponderado de food_rating y service_rating | Métrica compuesta de satisfacción |
| `preference_ambience_match` | Match entre preferencia de ambiente del usuario y del restaurante | Alineación de expectativas de experiencia |

### Construcción de Variable Objetivo

**Variable**: `rating` (calificación del usuario al restaurante)

**Transformación**: Se unificaron las calificaciones 1 y 2 en una sola categoría para mejorar el balance de clases y facilitar el análisis de WoE/IV.

**Distribución**:
- Rating 0: Muy insatisfecho
- Rating 1: Insatisfecho (incluye 1 y 2 originales)
- Rating 2: Satisfecho

### Limpieza de Datos

#### a) Normalización de Datos Categóricos

**Problema identificado**: Inconsistencias en datos de ubicación (San Luis Potosí, san luis potosi, S.L.P., slp)

**Solución aplicada**:
```python
# Proceso de normalización:
# 1. Convertir a minúsculas
# 2. Eliminar acentos (NFKD normalization)
# 3. Eliminar puntuación
# 4. Mapeo a valores estándar
```

**Impacto de negocio**: Datos geográficos consistentes permiten análisis regional correcto.

---

#### b) Manejo de Valores Especiales

**Valores identificados como faltantes**:
- `"?"` en variables: smoker, dress_preference, ambience, transport, etc.
- `"none"` en variables: interest, religion, smoking_area
- `"no"` en variable: url

**Estrategia aplicada**:
```python
df_nulos = clean_null_strings(df)
```

---

#### c) Variables Unarias (Eliminación)

**Criterio**: Variables con un solo valor único no aportan información.

**Variables eliminadas**:
- `country`: Solo "mexico"
- `fax`: 100% valores nulos

---

#### d) Variables Poco Pobladas

**Criterio**: Eliminar columnas con >65% de valores faltantes.

**Resultado**: Ninguna variable cumplió este criterio, todas se conservaron.

---

#### e) Tratamiento de Valores Ausentes

**Estrategia diferenciada por tipo de variable**:

| Tipo de Variable | Estrategia | Variables Ejemplo |
|------------------|------------|-------------------|
| **Alta cardinalidad** | Categoría "desconocido" | address, zip, Rcuisine |
| **Categóricas (muchos nulos)** | Categoría "desconocido" | smoker |
| **Categóricas (pocos nulos)** | Moda | dress_preference, transport |
| **Numéricas enteras** | Mediana | age, num_visits |
| **Numéricas decimales** | Media | price, distance |

**Justificación de negocio**:
- La moda preserva la distribución categórica original
- La mediana es robusta a outliers en variables enteras
- La media es adecuada para variables con distribución normal

---

#### f) Detección y Remoción de Outliers

**Método aplicado**: Intersección de IQR y Z-score (z_threshold=3, iqr_factor=1.5)

**Variables analizadas**:
- `weight`, `height`: Características físicas
- `age`: Edad del usuario
- `dist_user_restaurant`: Distancia calculada
- `restaurant_popularity`: Popularidad

**Resultado**: Se conservó el **88.4%** de los datos originales.

**Impacto de negocio**: Eliminación de casos extremos que distorsionarían el análisis sin perder representatividad de la muestra.

---

#### g) Multicolinealidad

**Criterio**: Eliminar variables con correlación perfecta (|r| = 1.0)

**Variables eliminadas**:
- `birth_year`: Correlación 1.0 con `age` (ya creada)

**Variables conservadas**:
- `latitude_user`, `longitude_user`: Aunque correlacionadas, se usan para calcular distancia

**Justificación**: Se eliminan solo redundancias perfectas, conservando información complementaria.

---

### Reducción de Dimensiones

#### PCA (Análisis de Componentes Principales)

**Configuración**:
- Scaler: `StandardScaler` (requisito teórico de PCA)
- Componentes: 2
- Variables incluidas: Todas las numéricas excepto ratings y IDs

**Resultados**:
- **Varianza explicada**: 46% con 2 componentes
- **Interpretación**: Necesitaríamos más componentes para el 90% (teoría)

**Hallazgos visuales**:
- Se observan **3 clusters** bien definidos
- La variable objetivo muestra tendencias diferenciadas por cluster
- Cluster derecho: Mayor concentración de calificaciones bajas

**Variables con mayor carga**:
- PC1: `latitude_user`, `longitude_user`, `dist_user_restaurant`
- PC2: `height`, `latitude_rest`, `longitude_rest`

**Insight de negocio**: La geografía (ubicación de usuario y restaurante) explica gran parte de la variabilidad en los datos.

---

#### VarClusHi (Clustering de Variables)

**Propósito**: Identificar grupos de variables altamente correlacionadas y seleccionar representantes.

**Resultados principales**:

| Cluster | Variables Principales | R² Propio | Interpretación |
|---------|----------------------|-----------|----------------|
| 0 | latitude_user, longitude_user | 0.97 | Ubicación del usuario |
| 1 | latitude_rest, longitude_rest | 0.94 | Ubicación del restaurante |
| 2 | height, weight, ratings | 0.83 | Características físicas y evaluación |

**Métricas clave**:
- **RS_Own**: Qué tan bien se explica la variable por su cluster (alto = bueno)
- **RS_NC**: Qué tanto se explica por otro cluster (bajo = bueno)
- **RS_Ratio = RS_NC / RS_Own**: Ratio bajo = buena ubicación

**Variables recomendadas para eliminación**:

| Variable | RS_Ratio | Motivo |
|----------|----------|--------|
| restaurant_popularity | 0.702 | Muy mal explicada por su cluster |
| age | 0.915 | No pertenece claramente a ningún cluster |
| dist_user_restaurant | 0.879 | Multicolineal con coordenadas |
| weight | 0.865 | Contribución débil |

**Decisión de negocio**: Conservar representantes de cada cluster para mantener diversidad de información sin redundancia.

---

#### SelectKBest (Poder Predictivo)

**Configuración**:
- Función de score: `f_classif` (ANOVA F-value)
- K = 5 mejores variables
- Encoding: OneHotEncoder para categóricas

**Top 5 variables seleccionadas**:

| Ranking | Variable | Score F | Interpretación de Negocio |
|---------|----------|---------|---------------------------|
| 1 | color_purple | 245.67 | Usuarios con preferencia de color púrpura tienden a calificar mejor |
| 2 | hijos_kids | 198.43 | Familias con niños tienen patrones de calificación distintos |
| 3 | height | 156.22 | Posible intermediario de otras características demográficas |
| 4 | personality_hunter-ostentatious | 134.18 | Personalidad audaz asociada con expectativas diferentes |
| 5 | transport_on_foot | 121.56 | Usuarios que caminan (cercanía) califican diferente |

**Insight estratégico**: Las preferencias personales (color, personalidad) son más predictivas que características físicas del restaurante.

---

#### WoE e IV (Transformación Entrópica)

**Top 10 variables por Information Value**:

| Ranking | Variable | IV | Nivel | Insight de Negocio |
|---------|----------|----|----|---------------------|
| 1 | **color** | 4.66 | Extraordinaria | Fuerte asociación entre preferencia de color y satisfacción |
| 2 | **hijos** | 3.42 | Extraordinaria | Familias tienen necesidades específicas |
| 3 | **personality** | 2.73 | Extraordinaria | Personalidad influye en expectativas |
| 4 | **interest** | 2.65 | Extraordinaria | Intereses gastronómicos predicen satisfacción |
| 5 | **transport** | 2.03 | Extraordinaria | Medio de transporte relacionado con distancia/comodidad |
| 6 | **budget** | 1.91 | Extraordinaria | Presupuesto vs precio influye en percepción de valor |
| 7 | **preference_ambience_match** | 1.66 | Extraordinaria | Match de ambiente es crítico |
| 8 | **drink_level** | 1.60 | Extraordinaria | Hábitos de consumo relacionados con satisfacción |
| 9 | **ambience** | 1.75 | Extraordinaria | Ambiente deseado vs ofrecido |
| 10 | **dress_preference** | 1.47 | Extraordinaria | Código de vestimenta refleja formalidad esperada |

**Ejemplo de WoE - Variable "color"**:

| Categoría | WoE | Interpretación |
|-----------|-----|----------------|
| purple | +1.20 | Usuarios con preferencia púrpura califican **MUY POSITIVAMENTE** |
| red | +0.45 | Califican positivamente |
| yellow | -0.80 | Califican negativamente |
| Missing | -0.05 | Neutral |

**Recomendación de negocio**: Segmentar usuarios por preferencias personales para personalizar experiencia.

---

## Conclusiones y Recomendaciones

### Hallazgos Técnicos

1. **Multicolinealidad geográfica**: Las coordenadas (latitud/longitud) dominan la varianza del dataset
2. **Variables personales > Variables del restaurante**: Las preferencias individuales son más predictivas
3. **Segmentación clara**: Se identifican 3 perfiles de usuarios distintos

### Hallazgos de Negocio

#### Factores Clave de Satisfacción

1. **Match de preferencias** (IV: 1.66)
   - El alineamiento entre lo que el usuario busca (ambiente, cocina) y lo que ofrece el restaurante es crítico
   - **Acción**: Implementar sistema de recomendación basado en preferencias

2. **Perfil demográfico** (hijos: IV 3.42)
   - Familias con niños tienen necesidades específicas (menú infantil, espacio, ruido)
   - **Acción**: Segmentar marketing para familias vs adultos

3. **Personalidad del usuario** (IV: 2.73)
   - Usuarios audaces/cazadores buscan experiencias diferentes
   - **Acción**: Desarrollar menús de "experiencias" para este segmento

4. **Accesibilidad** (transport: IV 2.03, distancia)
   - Usuarios que caminan califican diferente (posiblemente mejor por cercanía)
   - **Acción**: Marketing hiperlocal para atraer vecinos

#### Recomendaciones Estratégicas

**Para Restaurantes**:
1. Definir claramente el perfil de cliente objetivo (ambiente, precio, tipo de cocina)
2. Asegurar consistencia entre promesa de marca y experiencia real
3. Ofrecer opciones para familias si es parte del target
4. Invertir en presencia local (usuarios cercanos son más leales)

**Para Plataformas de Recomendación**:
1. Ponderar más las preferencias personales que las características físicas
2. Implementar filtros de "match" entre usuario y restaurante
3. Considerar distancia como factor crítico
4. Segmentar recomendaciones por presencia de niños

**Para Análisis Futuros**:
1. Incorporar datos temporales (hora, día, estación)
2. Analizar interacción entre variables (ej: presupuesto × precio)
3. Construir modelo predictivo con las variables seleccionadas
4. Validar hallazgos con pruebas A/B

---

## Próximos Pasos

1. **Modelado Predictivo**
   - Entrenar Random Forest / XGBoost con variables seleccionadas
   - Validación cruzada y tunning de hiperparámetros
   - Interpretación con SHAP values

2. **Segmentación de Usuarios**
   - K-means clustering sobre componentes PCA
   - Perfiles detallados por segmento
   - Estrategias de engagement específicas

3. **Sistema de Recomendación**
   - Filtrado colaborativo usuario-restaurante
   - Incorporar scores de WoE en algoritmo
   - A/B testing de recomendaciones

4. **Dashboard Ejecutivo**
   - Visualizaciones interactivas con Streamlit/Dash
   - Métricas de negocio en tiempo real
   - Simulador de "qué pasaría si"

---

## Juan Miguel Galan Olivares

**Diplomado en Ciencia de Datos - Módulo 1**

Proyecto de examen desarrollado aplicando técnicas avanzadas de:
- Ingeniería de características
- Limpieza y preprocesamiento de datos
- Análisis exploratorio multivariado
- Reducción de dimensionalidad
- Selección de variables
- Transformación entrópica (WoE/IV)

---

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

**Copyright © 2025 Juan Miguel Galan Olivares**

---

**Última actualización**: Diciembre 2025
