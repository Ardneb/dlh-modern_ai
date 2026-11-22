#!/usr/bin/env python3
"""
Function initializes and returns an untrained boosting
classifier based on the specified algorithm name
"""
from sklearn import ensemble
import xgboost as xgb
import lightgbm as lgb


def compare_boosting_classifiers(name, n_estimators, random_state):
    """
    Returns a boosting classifier based on the specified algorithm name
    """
    if name == 'adaboost':
        return ensemble.AdaBoostClassifier(
            n_estimators=n_estimators,
            random_state=random_state
        )
    elif name == 'gradient_boosting':
        return ensemble.GradientBoostingClassifier(
            n_estimators=n_estimators,
            random_state=random_state
        )
    elif name == 'xgboost':
        return xgb.XGBClassifier(
            n_estimators=n_estimators,
            random_state=random_state
        )
    elif name == 'lightgbm':
        return lgb.LGBMClassifier(
            n_estimators=n_estimators,
            random_state=random_state,
            verbose=-1
        )
    else:
        raise ValueError(f"Unknown model name '{name}'")
