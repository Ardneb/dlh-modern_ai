#!/usr/bin/env python3
"""
Function Apply_PCA(X, n_components, random_state)
that performs Principal Component Analysis (PCA)
on tabular data using Scikit-learn
"""
from sklearn import decomposition


def Apply_PCA(X, n_components, random_state):
    """
    Performs Principal Component Analysis (PCA)
    on tabular data by reducing the dimensionality
    of the data to n_components
    """
    pca = decomposition.PCA(n_components=n_components,
                            random_state=random_state)
    X_pca = pca.fit_transform(X)
    return X_pca, pca
