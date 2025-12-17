import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_selection import SelectKBest, f_classif
import plotly.graph_objects as go

def poder_predictivo(X: pd.DataFrame, y, num_k: int):
    """
    Calcula el poder predictivo de las variables usando SelectKBest (f_classif),
    aplicando OneHotEncoder a las categóricas y dejando pasar las numéricas.

    Parameters
    ----------
    X : pd.DataFrame
        DataFrame con las variables explicativas.
    y : array-like
        Variable objetivo (clase).
    num_k : int
        Número de variables a seleccionar (k de SelectKBest).

    Returns
    -------
    data_poder_predictivo : pd.DataFrame
        DataFrame con las k variables seleccionadas ya transformadas.
    scores : pd.DataFrame
        DataFrame con todas las variables (después del preprocesamiento)
        y su score de SelectKBest, ordenadas de mayor a menor.
    selected_features : np.ndarray
        Arreglo con los nombres de las k variables seleccionadas.
    fig : plotly.graph_objs._figure.Figure
        Figura de Plotly con el gráfico de barras de los scores.
    """

    # Separar columnas numéricas y categóricas
    num_cols = X.select_dtypes(include=['int64', 'float64']).columns
    cat_cols = X.select_dtypes(include=['object', 'category', 'string']).columns

    preprocess = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(drop='first'), cat_cols),
            ('num', 'passthrough', num_cols)
        ]
    )

    # matriz preprocesada (CSR)
    X_pre = preprocess.fit_transform(X)

    selector = SelectKBest(score_func=f_classif, k=num_k)
    X_new = selector.fit_transform(X_pre, y)      # CSR (n_muestras, k)

    feature_names = preprocess.get_feature_names_out()
    selected_features = feature_names[selector.get_support()]

    # 👉 convertir a array denso antes del DataFrame
    X_new_dense = X_new.toarray()

    data_poder_predictivo = pd.DataFrame(
        X_new_dense,
        columns=selected_features
    )

    scores = pd.DataFrame({
        "feature": feature_names,
        "score": selector.scores_
    }).sort_values(by="score", ascending=False)

    fig = go.Figure([
        go.Bar(x=scores['feature'], y=scores['score'])
    ])
    fig.update_layout(
        title="Scores (SelectKBest)",
        xaxis_title="Variables",
        yaxis_title="Score"
    )

    return data_poder_predictivo, scores, selected_features, fig