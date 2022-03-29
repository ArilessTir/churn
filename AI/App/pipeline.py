from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from preprocessor import preprocessor


Log_reg = Pipeline(
    steps=[
        ('preprocessing', preprocessor),
        ('model', LogisticRegression(
            C=10, random_state=400, n_jobs=-1, max_iter=300))
    ]
)
