#!/usr/bin/env python3
"""Function engineers new features from the dataset"""
import pandas as pd


def create_features(df):
    """
    Creates:
    NumServices: Number of services the customer
    is subscribed to (counting only those with
    'Yes' in selected service-related columns)
    TenureGroup: A categorical column that bins
    the tenure into intervals: 0-12, 13-24, 25-48,
    49-60, 60+ , where 0 is excluded and upper bounds
    are inclusive
    Drops the original columns that were used to create
    the new ones
    """

    df = df.copy()

    service_cols = [
        'MultipleLines',
        'OnlineSecurity',
        'OnlineBackup',
        'DeviceProtection',
        'TechSupport',
        'StreamingTV',
        'StreamingMovies',
    ]

    num_services = pd.Series(0, index=df.index)
    for col in service_cols:
        if col in df.columns:
            num_services += (df[col] == 'Yes').astype(int)

    if 'InternetService' in df.columns:
        num_services += (
            df['InternetService'].isin(['DSL', 'Fiber optic']).astype(int)
        )
    df['NumServices'] = num_services

    bins = [0, 12, 24, 48, 60, float('inf')]
    labels = ['0-12', '13-24', '25-48', '49-60', '60+']

    if 'tenure' in df.columns:
        df['TenureGroup'] = pd.cut(df['tenure'], bins=bins, labels=labels)

    cols_to_drop = service_cols + ['InternetService', 'tenure']
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

    return df
