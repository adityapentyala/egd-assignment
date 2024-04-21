import pandas as pd 
import numpy as np 
from tabulate import tabulate

earliest_year=1985
metrics = ["GDP (current LCU)", "GDP per capita (current US$)", "Gross savings (% of GDP)", 
        "Taxes less subsidies on products (current US$)",
        "Fuel exports (% of merchandise exports)", "Labor force, total",
        "Military expenditure (current USD)"]

def get_data(filepath: str, save: bool=False, get_train: bool=True, get_test: bool=True):
    excel_data = pd.read_excel(filepath, usecols=list(range(2, 67)), skiprows=2)
    excel_data.columns = excel_data.iloc[0]
    excel_data = excel_data[1:]
    years = list(range(earliest_year, 2015, 5))
    test_years = list(range(earliest_year+1, 2015, 5))
    excel_data.set_index("Indicator Name", inplace = True)
    filtered_data = excel_data.loc[metrics, years]
    test_filtered = excel_data.loc[metrics, test_years]
    #print(filtered_data)
    #print(filtered_data.columns)
    test_filtered = test_filtered.transpose()
    filtered_data = filtered_data.transpose()
    if save and get_test:
        test_filtered.to_excel(f"{filepath}_test_clean.xlsx")
    if save and get_train:
        filtered_data.to_excel(f"{filepath}_clean.xlsx")
    print(f"written succesfully to {filepath}!")


def print_equation(metrics, coeffs, intercept):
    print('GDP growth rate = {:.2e}'.format(intercept), end=" ")
    print("+", end=" ")
    for i in range(len(metrics)):
        print("{beta:.2e}({metric})".format(metric=metrics[i],beta=coeffs[i]), end=" ")
        print("+", end=" ")
    print()

def print_stat_table(metrics, coeffs, intercept):
    new_metrics = ['Y-Intercept']
    new_metrics.extend(metrics)
    betas = [intercept]
    betas.extend(coeffs)
    data = []
    for i in range(len(new_metrics)):
        data.append((new_metrics[i], betas[i]))
    table = tabulate(data, headers=['METRIC', 'BETA'])
    print(table)