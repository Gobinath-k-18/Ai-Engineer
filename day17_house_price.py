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
    "Area": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000, 3200],
    "Bedrooms": [2, 2, 3, 3, 4, 4, 4, 5, 5, 5],
    "Age": [10, 8, 5, 6, 3, 4, 2, 3, 1, 2],
    "Price": [40, 45, 60, 70, 82, 88, 95, 110, 125, 135]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# 2. Separate features and target
X = df[["Area", "Bedrooms", "Age"]]
y = df["Price"]

# 3. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 4. Create model
model = LinearRegression()

# 5. Train model
model.fit(X_train, y_train)

print("\nModel trained successfully!")

# 6. Make predictions
predictions = model.predict(X_test)

print("\nPredicted Prices:")
print(predictions)

print("\nActual Prices:")
print(y_test.values)

# 7. Evaluate model
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, predictions)

print("\nModel Metrics:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)