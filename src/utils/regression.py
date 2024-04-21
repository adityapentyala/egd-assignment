from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.utils import Bunch

lr = LinearRegression()

def create_regression_data(df):
    data = Bunch(data=df.drop(['Unnamed: 0'], axis=1).values,
            target=df['GDP growth'].values)
    return data, df.columns

def find_regression_params(data):
    lr = LinearRegression()
    lr.fit(data['data'], data['target'])
    return lr.coef_, lr.intercept_, lr.score(data['data'], data['target'])
    