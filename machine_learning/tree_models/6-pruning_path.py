#!/usr/bin/env python3
"""
Function retrieves the cost-complexity pruning
path for a given decision tree classifier
"""


def get_pruning_path(clf, X, y):
    """
    Retrieves the cost-complexity pruning path
    for a given decision tree classifier.
    """
    path = clf.cost_complexity_pruning_path(X, y)
    return path.cpp_alphas, path.impurities
