import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# Define the training data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([5, 7, 9, 11, 13])

# Create a linear regression model and fit it to the data
model = LinearRegression()
model.fit(X, y)

# Save the model using joblib
joblib.dump(model, 'model.pkl')
