#!/usr/bin/env python3

"""
Function generates predictions from a trained
tree-based classifier using Scikit-learn
"""


def generate_predictions(clf, X):
    """
    Generates predictions from a trained
    tree-based classifier using Scikit-learn
    """
    return clf.predict(X)
