import pandas as pd

# 1. Create student dataset
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

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)

# 3. Split data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Features:")
print(X_train)

print("\nTesting Features:")
print(X_test)

print("\nTraining Target:")
print(y_train)

print("\nTesting Target:")
print(y_test)

# 4. Create the KNN model
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)

# 5. Train the model
model.fit(X_train, y_train)

print("\nKNN model trained successfully!")

# 6. Make predictions
predictions = model.predict(X_test)

print("\nPredicted Results:")
print(predictions)

print("\nActual Results:")
print(y_test.values)

# 7. Compare different K values
from sklearn.metrics import accuracy_score

for k in [1, 3, 5]:
    model = KNeighborsClassifier(n_neighbors=k)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\nK = {k}")
    print("Predictions:", predictions)
    print("Actual:", y_test.values)
    print("Accuracy:", accuracy)
    # 8. Apply feature scaling
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nScaled Training Features:")
print(X_train_scaled)

print("\nScaled Testing Features:")
print(X_test_scaled)
# 9. Compare scaled and unscaled KNN
from sklearn.metrics import accuracy_score

for k in [1, 3, 5]:
    # Model without scaling
    model_original = KNeighborsClassifier(n_neighbors=k)
    model_original.fit(X_train, y_train)
    pred_original = model_original.predict(X_test)

    accuracy_original = accuracy_score(y_test, pred_original)

    # Model with scaling
    model_scaled = KNeighborsClassifier(n_neighbors=k)
    model_scaled.fit(X_train_scaled, y_train)
    pred_scaled = model_scaled.predict(X_test_scaled)

    accuracy_scaled = accuracy_score(y_test, pred_scaled)

    print(f"\nK = {k}")
    print("Without scaling:", pred_original)
    print("Without scaling accuracy:", accuracy_original)
    print("With scaling:", pred_scaled)
    print("With scaling accuracy:", accuracy_scaled)