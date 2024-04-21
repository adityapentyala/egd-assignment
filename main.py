from utils import data_utils, regression
import argparse

from utils import regression

#utils.get_data("data/worldbank_venezuela_data.xls", get_train=False, save=True)

gdp_2020 = 4090500000000
gdp_2010 = 1016834748000
dataset, columns = regression.create_train_data("data\worldbank_venezuela_data.xls_clean.xlsx", gdp_2020)
test_dataset, test_columns = regression.create_train_data("data\worldbank_venezuela_data.xls_test_clean.xlsx", gdp_2010)

#print(dataset)
metrics = list(columns[2:])
#print(metrics)

score, coeffs, intercept, test_score = regression.find_regression_params(dataset, test_dataset)
print(f"R2 score: {score}\n", f"coeffs: {list(coeffs)}\n", f"intercept: {intercept}\n")

print(f"test R2 score: {test_score}")

data_utils.print_equation(metrics, coeffs, intercept)
print()
data_utils.print_stat_table(metrics, coeffs, intercept)

"""if __name__ == "__main__()":
    parser = argparse."""