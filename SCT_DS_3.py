# Build the Decision Tree Classifier with min_samples_split and min_samples_leaf
clf = DecisionTreeClassifier(random_state=42, max_depth=3, min_samples_split=20, min_samples_leaf=10)
clf.fit(X_train, y_train)

# Visualize the Decision Tree
plt.figure(figsize=(15,10))
tree.plot_tree(clf, filled=True, feature_names=X.columns, class_names=['no', 'yes'], rounded=True)
plt.show()