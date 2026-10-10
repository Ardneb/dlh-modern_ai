#!/usr/bin/env python3
"""Function visualising missing values in a DataFrame"""
import matplotlib.pyplot as plt
import numpy as np


def plot_missingness(df):
    """
    Visualizes missing values in a DataFrame using scatter plot.
    """
    plt.figure(figsize=(12, 8))

    rows, cols = np.where(df.isna())
    plt.title("Missingness Plot")
    plt.scatter(rows, cols, marker='|')
    plt.yticks(ticks=range(len(df.columns)), labels=df.columns)

    plt.tight_layout()
    plt.show()
