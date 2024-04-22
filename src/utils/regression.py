from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.utils import Bunch

lr = LinearRegression()

def create_regression_data(df):
    data = Bunch(data=df.drop(columns=['Unnamed: 0', 'gdp growth rate', 'GDP', 'Military expenditure (current USD)'], axis=1).values,
            target=df['gdp growth rate'].values)
    return data, df.drop(['Unnamed: 0', 'gdp growth rate', 'GDP', 'Military expenditure (current USD)'], axis=1).columns

def find_regression_params(data):
    lr = LinearRegression()
    lr.fit(data['data'], data['target'])
    return lr.coef_, lr.intercept_, lr.score(data['data'], data['target'])
    