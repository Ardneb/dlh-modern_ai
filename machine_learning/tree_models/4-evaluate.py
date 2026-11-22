#!/usr/bin/env python3
"""Function generates a detailed classification report using Scikit-learn"""
from sklearn import metrics


def evaluate(true_labels, predicted_labels, class_names):
    """
    Generates a detailed classification report using Scikit-learn
    """
    report = metrics.classification_report(
        y_true=true_labels,
        y_pred=predicted_labels,
        target_names=class_names
    )
    return report
