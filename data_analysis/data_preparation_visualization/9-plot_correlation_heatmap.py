#!/usr/bin/env python3
"""
Function visualizing correlations between
continuous numeric features using seaborn
"""
import seaborn as sns
import matplotlib.pyplot as plt


def plot_correlation_heatmap(df):
    """
    Computes and visualizes pairwise
    correlations between continuous numeric
    features using a Seaborn heatmap
    """
    plt.figure(figsize=(6, 5))
    corr_matrix = df.select_dtypes(include='number').corr()
    sns.heatmap(corr_matrix,
                annot=True,
                cmap='coolwarm',
                vmin=-1,
                vmax=1
                )
    plt.title("Correlation Matrix")
    plt.show()
