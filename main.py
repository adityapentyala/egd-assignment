from src import utils, regression

#utils.get_data("data/worldbank_venezuela_data.xls")

gdp_2020 = 4090500000000
dataset, columns = regression.create_train_data("data\worldbank_venezuela_data.xls_clean.xlsx", gdp_2020)
#print(dataset)
metrics = list(columns[2:])
#print(metrics)

score, coeffs, intercept = regression.find_regression_params(dataset)
print(f"R2 score: {score}\n", f"coeffs: {list(coeffs)}\n", f"intercept: {intercept}\n")

utils.print_equation(metrics, coeffs, intercept)
print()
utils.print_stat_table(metrics, coeffs, intercept)



#penti is gay