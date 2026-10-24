#!/usr/bin/env python3
"""Function encodes features for modeling using Scikit-learn"""
import pandas as pd
from sklearn import preprocessing


def encode_features(df):
    """
    The function should encode:
    Churn: LabelEncoder (No→0, Yes→1)
    Partner, Dependents, PaperlessBilling, SeniorCitizen:
    OrdinalEncoder (No→0, Yes→1)
    Contract, PaymentMethod: One-hot encoding with drop first set to True
    TenureGroup: Alphabetical order OrdinalEncoder
    """

    df = df.copy()
    le_churn = preprocessing.LabelEncoder()
    if 'Churn' in df.columns:
        df['Churn'] = le_churn.fit_transform(df['Churn'])

    binary_cols = [
            'Partner', 'Dependents', 'PaperlessBilling', 'SeniorCitizen'
        ]
    oe_binary = preprocessing.OrdinalEncoder(categories=[['No', 'Yes']])

    for col in binary_cols:
        if col in df.columns:
            df[col] = oe_binary.fit_transform(df[[col]]).astype(int).ravel()

    ohe_cols = ['Contract', 'PaymentMethod']
    existing_ohe = [col for col in ohe_cols if col in df.columns]

    if existing_ohe:
        df = pd.get_dummies(
            df, columns=existing_ohe, drop_first=True, dtype=int
        )

    oe_tenure = preprocessing.OrdinalEncoder()
    if 'TenureGroup' in df.columns:
        df[['TenureGroup']] = oe_tenure.fit_transform(df[['TenureGroup']])

    return df, le_churn, oe_binary, oe_tenure
