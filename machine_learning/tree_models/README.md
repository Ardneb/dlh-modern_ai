### 0. Decision Tree Classifier
Write a function build_decision_tree(min_samples_leaf, min_samples_split, random_state) to create a decision tree classifier using Scikit-learn
### 1. Train a Tree-Based Classifier
Write a function train_tree(clf, X, y) to train a tree-based classifier using Scikit-learn
### 2. View the Decision Rules of a Trained Tree
Write a function draw(clf, feature_names, class_names) that displays the textual structure of a trained decision tree classifier using Scikit-learn
### 3. Generate Predictions
Write a function generate_predictions(clf, X) to generate predictions from a trained tree-based classifier using Scikit-learn
### 4. Evaluate Classifier Performance
Write a function evaluate(true_labels, predicted_labels, class_names) that generates a detailed classification report using Scikit-learn
### 5. Pre-Pruning
Write a function prepruning(X, y, clf) that uses Scikit-learn to perform a Grid Search for the best pre-pruning hyperparameters for a decision tree classifier
### 6. (Post-Pruning) Retrieve the Pruning Path of a Decision Tree
Write a function get_pruning_path(clf, X, y) that retrieves the cost-complexity pruning path for a given decision tree classifier
### 7. (Post-Pruning) Train and Evaluate Decision Trees with Pruning
Write a function prune_and_evaluate_trees(X_train, y_train, X_test, y_test, ccp_alphas, random_state, min_samples_leaf, min_samples_split) that trains multiple decision tree classifiers over a range of cost-complexity pruning parameters (ccp_alpha) and evaluates their performance
### 8. (Post-Pruning) Best ccp_alpha for Pruning
Write a function get_best_alpha(clfs, train_scores, test_scores, ccp_alphas) that selects the best pruning value ccp_alpha for a set of trained decision trees
### 9. Random Forest Classifier
Write a function random_forest(n_estimators, random_state) to create a random forest classifier using Scikit-learn
### 10. Feature Importance with Random Forest
Write a function feature_importance(rf) that computes and returns the feature importances from a trained random forest model