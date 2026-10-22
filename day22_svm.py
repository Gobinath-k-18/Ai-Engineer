
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# 1. Create the dataset
data = {
    "StudyHours": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 88, 92, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)
print("\nDataset shape:", df.shape)

# 2. Separate features and target
X = df[["StudyHours", "Attendance"]]
y = df["Pass"]

# 3. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining features:", X_train.shape)
print("Testing features:", X_test.shape)

# 4. SVM WITHOUT scaling
svm_model = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale"
)

svm_model.fit(X_train, y_train)

y_pred = svm_model.predict(X_test)

print("\n--- SVM WITHOUT SCALING ---")
print("Actual labels:", y_test.tolist())
print("Predicted labels:", y_pred.tolist())
print("Test accuracy:", accuracy_score(y_test, y_pred))

# 5. Scale the features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 6. SVM WITH scaling
svm_scaled = SVC(
    kernel="rbf",
    C=1.0,
    gamma="scale"
)

svm_scaled.fit(X_train_scaled, y_train)

y_pred_scaled = svm_scaled.predict(X_test_scaled)

print("\n--- SVM WITH SCALING ---")
print("Actual labels:", y_test.tolist())
print("Predicted labels:", y_pred_scaled.tolist())
print("Test accuracy:", accuracy_score(y_test, y_pred_scaled))

# 7. Compare both models
print("\n========== SVM COMPARISON ==========")

print(
    "Without scaling:",
    accuracy_score(y_test, y_pred)
)

print(
    "With scaling:",
    accuracy_score(y_test, y_pred_scaled)
)
