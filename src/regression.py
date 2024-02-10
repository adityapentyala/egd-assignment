from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.utils import Bunch

lr = LinearRegression()

def create_train_data(filepath, latest_gdp: int):
    df = pd.read_excel(filepath)
    data = Bunch(data=df.drop(['Year','GDP (current LCU)'], axis=1).values,
            target=df['GDP (current LCU)'].values)
    gdp_growth = []
    #print(data['target'])
    for i in range(0, len(data['target'])-1):
        gdp_growth.append((data['target'][i+1]-data['target'][i])/data['target'][i])
    gdp_growth.append((latest_gdp-data['target'][-1])/data['target'][-1])
    data['target'] = np.array(gdp_growth, dtype=np.float64)
    #print(data)
    return data, df.columns

def find_regression_params(data):
    lr = LinearRegression()
    lr.fit(data['data'], data['target'])
    return lr.score(data['data'], data['target']), lr.coef_, lr.intercept_