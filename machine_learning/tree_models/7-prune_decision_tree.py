#!/usr/bin/env python3
"""
Function that trains multiple decision tree
classifiers over a range of cost-complexity
pruning parameters and evaluates their performance
"""
from sklearn import tree
train_tree = __import__('1-train').train_tree


def prune_and_evaluate_trees(
        X_train,
        y_train,
        X_test,
        y_test,
        ccp_alphas,
        random_state,
        min_samples_leaf,
        min_samples_split
):
    """
    Trains multiple decision tree classifiers over a range of
    cost-complexity pruning parameters and evaluates their performance
    """
    clfs = []
    train_scores = []
    test_scores = []

    for alpha in ccp_alphas:
        clf = train.DecisionTreeClassifier(
            random_state=random_state,
            min_samples_leaf=min_samples_leaf,
            min_samples_split=min_samples_split,
            ccp_alpha=alpha
        )

        train_tree(clf, X_train, y_train)

        clfs.append(clf)
        train_scores.append(clf.score(X_train, y_train))
        test_scores.append(clf.score(X_test, y_test))

    return clfs, train_scores, test_scores
