
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()

data = iris.data
target = iris.target
feature_names = iris.feature_names
target_names = iris.target_names
description = iris.DESCR

permutation = np.random.permutation(data.shape[0])

data_shuffled = data[permutation]
target_shuffled = target[permutation]

data_reduced = data_shuffled[7:]
target_reduced = target_shuffled[7:]

print(data_reduced.shape, target_reduced.shape)
print(data.shape, target.shape)

random_data = np.random.uniform(data.min(), data.max(), size=(7, 4))
random_target = np.random.randint(0, 3, size=7)

data_rounded = [[round(x, 1) for x in row] for row in random_data]
data = np.concatenate((data_reduced, data_rounded))

target = np.concatenate((target_reduced, random_target))
print(data.shape, target.shape)
print(data, target)


# Define the parameter grid
param_grid = {'max_depth': [3, 4, 5, 6, 7, 8, 9, 10],
              'min_samples_leaf': [1, 2, 3, 4, 5]}

model = DecisionTreeClassifier()

# Create the grid search object
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)

# Fit the grid search object to the data
grid_search.fit(data, target)

# Get the best hyperparameters
best_params = grid_search.best_params_
print(best_params)

best_score = grid_search.best_score_
print(best_score)


# Extract the best decision tree model
best_model = grid_search.best_estimator_

plt.figure(figsize=(15, 8))
plot_tree(best_model, feature_names=feature_names,
          class_names=target_names, filled=True, rounded=True)
plt.show()
###

iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.30, random_state=0)

model = LogisticRegression()

model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = model.score(X_test, y_test)
print(f"Accuracy LR: {accuracy:.2f}")


# Extract the first two features of the data
X = iris.data[:, :2]
y = iris.target
