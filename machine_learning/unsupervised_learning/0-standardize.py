#!/usr/bin/env python3
"""Function standardizes tabular data using Scikit-learn"""
from sklearn import preprocessing


def Standardize(X):
    """
    Standardizes tabular data by
    removing the mean and scaling
    """
    scaler = preprocessing.StandardScaler()
    return scaler.fit_transform(X)
