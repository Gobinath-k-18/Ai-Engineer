
import pandas as pd

data = {
    "StudyHours": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 88, 92, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print(df)

X = df[["StudyHours", "Attendance"]]
y = df["Pass"]

print("\nFeatures (X):")
print(X)

print("\nTarget (y):")
print(y)



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training features:", X_train.shape)
print("Testing features:", X_test.shape)

print("Training labels:", y_train.shape)
print("Testing labels:", y_test.shape)



from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=2,
    random_state=42
)

model.fit(X_train, y_train)

print("Decision Tree trained successfully!")



from sklearn.metrics import accuracy_score

y_pred = model.predict(X_test)

print("Actual results:", y_test.tolist())
print("Predicted results:", y_pred.tolist())

accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)



import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(12, 6))

plot_tree(
    model,
    feature_names=["StudyHours", "Attendance"],
    class_names=["Fail", "Pass"],
    filled=True,
    rounded=True
)

plt.title("Student Pass/Fail Decision Tree")
plt.show()





from sklearn.metrics import accuracy_score

for depth in [1, 2, 3, None]:
    tree = DecisionTreeClassifier(
        criterion="gini",
        max_depth=depth,
        random_state=42
    )

    tree.fit(X_train, y_train)

    train_pred = tree.predict(X_train)
    test_pred = tree.predict(X_test)

    train_accuracy = accuracy_score(y_train, train_pred)
    test_accuracy = accuracy_score(y_test, test_pred)

    print(f"\nMax Depth: {depth}")
    print(f"Training Accuracy: {train_accuracy:.2f}")
    print(f"Testing Accuracy:  {test_accuracy:.2f}")

