import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# 1. Create dataset
data = {
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 45, 50, 60, 65, 70, 78, 85]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# 2. Separate features and target
X = df[["StudyHours"]]
y = df["Marks"]

# 3. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:")
print(X_train)

print("\nTesting data:")
print(X_test)

# 4. Create model
model = LinearRegression()

# 5. Train model
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# 6. Make predictions
predictions = model.predict(X_test)

print("\nPredictions:")
print(predictions)

print("\nActual values:")
print(y_test.values)

# 7. Calculate regression metrics
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("\nRegression Metrics:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)