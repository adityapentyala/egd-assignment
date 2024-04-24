import pandas as pd
from statsmodels.api import tsa
from datetime import datetime
import numpy as np

def get_timeseries_dataset(df, ratios=False):
    X = df[["Year",
        "Natural Log of GDP per capita (current US$)",
        "Gross domestic savings (current US$)",
        "Labor force, total",
        "Net trade in goods and services (BoP, current US$)",
        "Consumer price index (2010 = 100)",
        "Foreign direct investment, net (BoP, current US$)", 
        "gdp growth rate"
    ]]
    if ratios:
        X["Gross domestic savings (current US$)"] = X["Gross domestic savings (current US$)"]/df["GDP"]
        X["Foreign direct investment, net (BoP, current US$)"] = X["Foreign direct investment, net (BoP, current US$)"]/df["GDP"]
        X["Net trade in goods and services (BoP, current US$)"] = X["Net trade in goods and services (BoP, current US$)"]/df["GDP"]
        X = X.rename(columns={"Net trade in goods and services (BoP, current US$)":"Net trade in goods and services (% of GDP)",
                              "Foreign direct investment, net (BoP, current US$)": "Foreign direct investment, net (% of GDP)",
                              "Gross domestic savings (current US$)":"Gross domestic savings (% of GDP)"})
    X["Year"] = pd.to_datetime(df["Year"], format="%Y", errors='coerce')
    X.set_index("Year", inplace=True)
    #X = X.resample('A').mean()
    #X = X.drop(columns=["Year"])
    y = X["gdp growth rate"]
    X = X.drop(columns=["gdp growth rate"])
    return X, y

def fit_arima_model(X, y, p=1, d=0, q=1):
    arima_model = tsa.ARIMA(y, X, (p, d, q)).fit()
    return arima_model
