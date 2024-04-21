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
    
def clean_data(file):
    df = pd.read_excel(file)
    columns_delete=["Country Name", "Country Code", "Series Code",
       "1973 [YR1973]", "1974 [YR1974]", "1975 [YR1975]", "1976 [YR1976]","1977 [YR1977]", "1978 [YR1978]", "1979 [YR1979]", "1980 [YR1980]",
       "1981 [YR1981]", "1982 [YR1982]", "1983 [YR1983]", "1984 [YR1984]", "1985 [YR1985]", "1986 [YR1986]", "1987 [YR1987]", "1988 [YR1988]",
       "1989 [YR1989]"]
    df=df.drop(columns=columns_delete)
    df=df.transpose()
    df.columns = df.iloc[0]
    df = df.iloc[pd.RangeIndex(len(df)).drop(0)]
    df["GDP per capita (current US$)"] = np.log(np.array(df["GDP per capita (current US$)"], dtype=np.float64))
    for col in df.columns:
     df[col] = np.array(df[col], dtype=np.float64)
    df.rename(columns={'GDP per capita (current US$)':'Natural Log of GDP per capita (current US$)'})
    outfile = file.split("raw.")[0].replace("raw", "clean") +"clean.xlsx"
    print(outfile)
    df.to_excel(outfile)
    print(f"Written to file {outfile}")
    
