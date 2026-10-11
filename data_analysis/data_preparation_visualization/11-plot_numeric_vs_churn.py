#!/usr/bin/env python3
"""Function that compares continuous numeric feature distributions by churn"""
import matplotlib.pyplot as plt


def plot_numeric_vs_churn(df, col):
    """
    Compares continuous numeric feature
    distributions split by Churn status
    """
    plt.figure(figsize=(12, 8))
    churn_no = df[df['Churn'] == 'No'][col].dropna()
    churn_yes = df[df['Churn'] == 'Yes'][col].dropna()
    plt.hist([churn_no, churn_yes], bins=30, label=['No', 'Yes'])
    plt.title(f"{col} Distribution by Churn")
    plt.xlabel(col)
    plt.ylabel("Count")
    plt.legend(title="Churn")
    plt.tight_layout
    plt.show()
