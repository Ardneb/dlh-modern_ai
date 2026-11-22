#!/usr/bin/env python3
"""
Function selects the best pruning value
ccp_alpha for a set of trained decision trees
"""


def get_best_alpha(clfs, train_scores, test_scores, ccp_alphas):
    """
    Returns a random forest classifier with the specified number of estimators
    and random state
    """
    best_idx = max(
        range(len(clfs)),
        key=lambda i: (
            test_scores[i],
            -abs(train_scores[i] - test_scores[i]),
            ccp_alphas[i]
        )
    )
    best_alpha = ccp_alphas[best_idx]
    best_clf = clfs[best_idx]

    return best_alpha, best_clf
