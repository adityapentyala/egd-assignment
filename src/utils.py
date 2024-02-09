import pandas as pd 
import numpy as np 

earliest_year=1985
metrics = ["GDP (current LCU)", "GDP per capita (current US$)", "Gross savings (% of GDP)", 
        "Taxes less subsidies on products (current US$)",
        "Fuel exports (% of merchandise exports)", "Labor force, total",
        "Military expenditure (current USD)"]

def get_data(filepath: str, save: bool=False):
    excel_data = pd.read_excel(filepath, usecols=list(range(2, 67)), skiprows=2)
    excel_data.columns = excel_data.iloc[0]
    excel_data = excel_data[1:]
    years = list(range(earliest_year, 2015, 5))
    excel_data.set_index("Indicator Name", inplace = True)
    filtered_data = excel_data.loc[metrics, years]
    print(filtered_data)
    print(filtered_data.columns)
    filtered_data = filtered_data.transpose()
    filtered_data.to_excel(f"{filepath}_clean.xlsx")
    print("written succesfully!")

    