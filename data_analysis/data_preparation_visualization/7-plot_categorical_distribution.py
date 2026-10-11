#!/usr/bin/env python3
"""Function visualizing categorical feature distributions"""
import matplotlib.pyplot as plt


def plot_categorical_distributions(df, columns_to_plot=None):
    """function plotting categorical feature distributions"""
    df = df.copy()
    if columns_to_plot is None:
        columns_to_plot = [
            col for col in df.select_dtypes(include=['object']).columns
            if col != 'Churn'
        ]
    else:
        columns_to_plot = list(columns_to_plot)

    columns_count = len(columns_to_plot)
    if columns_count == 0:
        return
    n_cols, n_rows = 3, (columns_count + 2) // 3
    fig, axes = plt.subplots(
        n_rows, n_cols, figsize=(15, 5*n_rows)
    )

    axes = axes.flatten()
    for i, col in enumerate(columns_to_plot):
        value_counts = df[col].value_counts()
        axes[i].bar(value_counts.index.tolist(), value_counts.values)
        axes[i].set_title(col)
        axes[i].tick_params(axis='x', rotation=45)

    for j in range(columns_count, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.savefig("Task_7.png")
    plt.show()
