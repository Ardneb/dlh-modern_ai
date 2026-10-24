#!/usr/bin/env python3
"""
Function performs chi-square tests
for categorical features, using SciPy
"""
import pandas as pd
from scipy import stats


def chi_square_tests(df):
    """
    Computes the Chi-square p-value to test
    the independence between each categorical
    feature and the target variable Churn
    """
    p_values = {}
    categorical_cols = [
        col for col in df.select_dtypes(include=['object',
                                                 'category']).columns
        if col != 'Churn'
    ]

    for col in categorical_cols:
        contigency_table = pd.crosstab(df[col], df['Churn'])

        _, p_val, _, _ = stats.chi2_contingency(contigency_table)
        p_values[col] = p_val
    return p_values
