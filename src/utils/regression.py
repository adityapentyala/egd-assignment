from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.utils import Bunch
from statsmodels.api import OLS, add_constant

def create_regression_data_sklearn(df):
    data = Bunch(data=df.drop(columns=['Year', 'gdp growth rate', 'GDP', 'Military expenditure (current USD)'], axis=1).values,
            target=df['gdp growth rate'].values)
    return data, df.drop(['Year', 'gdp growth rate', 'GDP', 'Military expenditure (current USD)'], axis=1).columns

def find_regression_params_sklearn(data):
    lr = LinearRegression()
    lr.fit(data['data'], data['target'])
    return lr.coef_, lr.intercept_, lr.score(data['data'], data['target'])
    
def create_regression_data_OLS(df):
    X = df[[
        "Natural Log of GDP per capita (current US$)",
        "Gross domestic savings (current US$)",
        "Labor force, total",
        "Net trade in goods and services (BoP, current US$)",
        "Consumer price index (2010 = 100)",
        "Foreign direct investment, net (BoP, current US$)"
    ]]
    X = add_constant(X)
    y = df["gdp growth rate"]
    return X, y

def fit_model(X, y):
    model = OLS(y, X).fit()
    return model