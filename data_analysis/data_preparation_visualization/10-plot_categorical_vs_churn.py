#!/usr/bin/env python3
"""Function visualizing churn rates per category"""
import matplotlib.pyplot as plt


def plot_categorical_vs_churn(df, col):
    """ Visualizes churn rates per category in a DataFrame"""
    plt.figure(figsize=(12, 9))
    churn_rate = (df['Churn'] == 'Yes').groupby(df[col]).mean()
    plt.bar(churn_rate.index.astype(str), churn_rate.values)
    plt.title(f"Churn rate by {col}")
    plt.ylabel("Churn Rate")
    plt.xticks(rotation=45)

    plt.tight_layout
    plt.show()
