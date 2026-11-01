#!/usr/bin/env python3
"""
Function that evaluates K-Means clustering quality
using silhouette scores to measure cluster cohesion
and separation, and to compute the inertia to be used
for the elbow method
"""
from sklearn import metrics
K_Means = __import__('2-k_means').K_Means


def optimal_k(X, max_clusters, random_state):
    """
    Evaluates K-Means clustering quality using silhouette scores
    to measure cluster cohesion and separation, and to compute
    the inertia to be used for the elbow method
    """
    cluster_nums = []
    inertias = []
    silhouette_scores = []

    for k in range(2, max_clusters + 1):
        kmeans_model = K_Means(X, n_clusters=k, random_state=random_state)
        inertias.append(float(kmeans_model.inertia_))
        score = metrics.silhouette_score(X, kmeans_model.labels_)
        silhouette_scores.append(float(score))
        cluster_nums.append(k)

    return cluster_nums, inertias, silhouette_scores
