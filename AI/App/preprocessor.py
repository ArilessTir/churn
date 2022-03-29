from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, PolynomialFeatures, PowerTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from Config import CONFIG

preprocessor_int = Pipeline(
    steps=[
        ('Scaller', MinMaxScaler()),
        ('Poly', PolynomialFeatures(degree=5))
    ]
)


preprocessor = ColumnTransformer(
    transformers=[
        ('drop', 'drop', CONFIG['drop']),
        ('OHE', OneHotEncoder(), CONFIG['OHE']),
        ('Num', preprocessor_int, CONFIG['num']),
        ('passthrough', 'passthrough', CONFIG['passthrough'])
    ]
)
