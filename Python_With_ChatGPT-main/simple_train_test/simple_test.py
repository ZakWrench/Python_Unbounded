# Load the model using joblib
import joblib
import numpy as np
model = joblib.load('model.pkl')

# Use the model to make predictions
X_test = np.array([6, 7, 8]).reshape(-1, 1)
predictions = model.predict(X_test)
print(predictions)
