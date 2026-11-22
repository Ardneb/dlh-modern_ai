#!/usr/bin/env python3
"""Function creates a random forest classifier using Scikit-learn"""
from sklearn import ensemble


def random_forest(n_estimators, random_state):
    """
    Returns a random forest classifier with the specified number of estimators
    and random state
    """
    model = ensemble.RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )
    return model
