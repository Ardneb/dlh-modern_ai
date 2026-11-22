#!/usr/bin/env python3
"""
Function displays the textual structure of a 
trained decision tree classifier using Scikit-learn
"""


def draw(clf, feature_names, class_names):
    """
    Displays the textual structure of a trained
    decision tree classifier using Scikit-learn
    """
    rules = tree.export_text(
        clf,
        feature_names=list(feature_names),
        class_names=list(class_names)
    )
    print(rules)
