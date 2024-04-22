import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_plots(df):
    columns = df.columns
    for col in columns[1:]:
        fig, ax = plt.subplots()
        ax.plot(df["Year"], df[col])
        ax.title.set_text(f"{col} over time")
        ax.set_ylabel(col)
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.arange(start, end, 5))
        ax.set_xlabel("Year")

def plot_vs_gdp(df, growth_rate=False):
    r,c=3,2
    to_plot = "GDP"
    if growth_rate == True:
        to_plot="gdp growth rate"
    cols = [["Natural Log of GDP per capita (current US$)", "Gross domestic savings (current US$)"],
            ["Labor force, total", "Net trade in goods and services (BoP, current US$)"],
            ["Consumer price index (2010 = 100)", "Foreign direct investment, net (BoP, current US$)"]]
    for i in range(r):
        for j in range(c):
            fig, axs = plt.subplots()
            axs.scatter(df[cols[i][j]], df[to_plot])
            axs.title.set_text(f"{to_plot} vs {cols[i][j]}")
            axs.set_xlabel(cols[i][j])
            axs.set_ylabel(to_plot)