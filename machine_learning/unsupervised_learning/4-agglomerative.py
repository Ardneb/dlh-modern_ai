#!/usr/bin/env python3
"""
Function that performs Agglomerative hierarchical
clustering on tabular data using Scikit-learn
"""
from sklearn import cluster
from sklearn import metrics
Apply_PCA = __import__('1-pca').Apply_PCA


def Agglomerative_Clustering(
    X,
    n_clusters,
    random_state,
    n_components,
    use_pca_data=True
):
    """
    Creates and fits an Agglomerative Clustering model
    on tabular data by grouping the data into n_clusters clusters
    """
    if use_pca_data:
        data_used, _ = Apply_PCA(
            X,
            n_components=n_components,
            random_state=random_state
        )
    else:
        data_used = X

    model = cluster.AgglomerativeClustering(
        n_clusters=n_clusters,
        linkage='ward'
    )
    model.fit(data_used)

    if n_clusters > 1:
        score = float(metrics.silhouette_score(data_used, model.labels_))
    else:
        score = None

    return model, data_used, score
