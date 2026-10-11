#!/usr/bin/env python3
"""Function visualizing churn distribution"""
import matplotlib.pyplot as plt


def plot_churn_distribution(df):
    """function plotting churn distribution"""
    plt.figure(figsize=(12, 8))
    df = df.copy()
    churn_counts = df['Churn'].value_counts()
    churn_colors = {'No': 'skyblue', 'Yes': 'salmon'}
    colors = [churn_colors[val] for val in churn_counts.index]
    plt.bar(churn_counts.index, churn_counts.values, color=colors)
    plt.ylabel('Count')
    plt.title('Churn Distribution')
    plt.show()
