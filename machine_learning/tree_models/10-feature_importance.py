#!/usr/bin/env python3
"""
Function computes and returns the feature
importances from a trained random forest model
"""
import numpy as np


def feature_importance(rf):
    """
    Returns the feature importances from a trained random forest model
    """
    importances = rf.feature_importances_
    indices = np.argsort(importances)
    return importances, indices
