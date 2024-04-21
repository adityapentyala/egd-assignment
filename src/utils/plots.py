import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_plots(df):
    columns = df.columns
    for col in columns[1:]:
        fig, ax = plt.subplots()
        ax.plot(df[columns[0]], df[col])
        ax.title.set_text(f"{col} over time")
        ax.set_ylabel(col)
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.arange(start, end, 5))
        ax.set_xlabel("Year")
