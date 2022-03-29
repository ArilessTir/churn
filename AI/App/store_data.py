import os
from sqlalchemy import create_engine
import pandas as pd

os.environ['POSTGRESQL_USER'] = "user"
os.environ['POSTGRESQL_PASSWORD'] = "userpwd"
os.environ['POSTGRESQL_HOST_IP'] = "postgres_container"
os.environ['POSTGRESQL_PORT'] = '5432'
os.environ['POSTGRESQL_DATABASE'] = 'tuto'

engine = create_engine(
    'postgresql+psycopg2://' + os.environ['POSTGRESQL_USER'] + ':' + os.environ['POSTGRESQL_PASSWORD'] + '@' +
    os.environ['POSTGRESQL_HOST_IP'] + ':' +
    os.environ['POSTGRESQL_PORT'] + '/' + os.environ['POSTGRESQL_DATABASE'],
    echo=False)


def predictionOverview(df):
    df.to_sql(
        name='result',
        con=engine,
        if_exists="append",
        index=False,
        method='multi'
    )
    return '... Table créée'
