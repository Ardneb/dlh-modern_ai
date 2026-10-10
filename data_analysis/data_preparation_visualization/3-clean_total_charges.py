#!/usr/bin/env python3
"""Function handling missing values in the TotalCharges"""


def clean_total_charges(df, method='drop'):
    """
    Cleans the TotalCharges column by handling missing values.
    df: pandas DataFrame with missing values in TotalCharges
    method: Strategy to handle missing values:
    'drop': Remove rows with missing TotalCharges
    'median': Fill with column median
    'impute': Replace with MonthlyCharges * tenure
    """
    df = df.copy()

    if method == 'drop':
        df = df.dropna(subset=['TotalCharges'])
    elif method == 'median':
        median_value = df['TotalCharges'].median()
        df['TotalCharges'] = df['TotalCharges'].fillna(median_value)
    elif method == 'impute':
        impute_value = df['MonthlyCharges'] * df['tenure']
        df['TotalCharges'] = df['TotalCharges'].fillna(impute_value)
    return df
