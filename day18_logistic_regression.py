import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 1. Create dataset
data = {
    "StudyHours": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 88, 92, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)


# 2. Separate features and target
X = df[["StudyHours", "Attendance"]]
y = df["Pass"]


# 3. Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)


# 4. Create Logistic Regression model
model = LogisticRegression()


# 5. Train the model
model.fit(X_train, y_train)

print("\nModel trained successfully!")


# 6. Make predictions
predictions = model.predict(X_test)

print("\nPredicted Classes:")
print(predictions)

print("\nActual Classes:")
print(y_test.values)


# 7. Get prediction probabilities
probabilities = model.predict_proba(X_test)

print("\nPrediction Probabilities:")
print(probabilities)



accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:")
print(accuracy)