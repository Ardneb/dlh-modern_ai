#!/usr/bin/env python3
"""
Function creates and fits a K-Means clustering
model using Scikit-learn on tabular data
"""
from sklearn import cluster


def K_Means(X, n_clusters, random_state):
    """
    Creates and fits a K-Means clustering model
    on tabular data by grouping the data into
    n_clusters clusters
    """
    kmeans = cluster.KMeans(n_clusters=n_clusters,
                            random_state=random_state)
    kmeans.fit(X)
    return kmeans
