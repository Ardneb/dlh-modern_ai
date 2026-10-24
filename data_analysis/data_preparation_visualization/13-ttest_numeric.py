#!/usr/bin/env python3
"""
Function that performs Welch's t-tests
for continuous numeric features using scipy
"""
from scipy import stats


def ttest_numeric(df):
    """
    Computes t-test p-value comparing
    Churn=Yes vs Churn=No for each numeric feature
    """

    t_test = {}

    numeric_cols = [
        col for col in df.select_dtypes(include=['number']).columns
        if col != 'Churn'
    ]

    for col in numeric_cols:
        group_yes = df[df['Churn'] == 'Yes'][col].dropna()
        group_no = df[df['Churn'] == 'No'][col].dropna()

        _, p_val = stats.ttest_ind(group_yes, group_no, equal_var=False)

        t_test[col] = p_val

    return t_test
