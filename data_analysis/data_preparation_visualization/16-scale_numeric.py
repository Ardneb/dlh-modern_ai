#!/usr/bin/env python3
"""Function standardizes numeric columns"""
from sklearn import preprocessing


def scale_numeric(df):
    """
    Scales MonthlyCharges and TotalCharges
    using StandardScaler (mean=0, std=1)
    """
    scaler = preprocessing.StandardScaler()
    cols_to_scale = ['MonthlyCharges', 'TotalCharges']

    existing_cols = [col for col in cols_to_scale if col in df.columns]

    if existing_cols:
        df[existing_cols] = scaler.fit_transform(df[existing_cols])

    return df
