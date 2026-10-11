
import pandas as pd

data = {
    "StudyHours": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [60, 65, 70, 72, 75, 80, 85, 88, 92, 95],
    "Pass": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print(df)
print("\nDataset shape:", df.shape)


from sklearn.model_selection import train_test_split

X = df[["StudyHours", "Attendance"]]
y = df["Pass"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining features shape:", X_train.shape)
print("Testing features shape:", X_test.shape)
print("Training labels shape:", y_train.shape)
print("Testing labels shape:", y_test.shape)


from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

print("Random Forest trained successfully!")



from sklearn.tree import DecisionTreeClassifier

dt_model = DecisionTreeClassifier(
    max_depth=2,
    random_state=42
)

dt_model.fit(X_train, y_train)

print("Decision Tree trained successfully!")


from sklearn.metrics import accuracy_score

# Random Forest predictions
rf_train_pred = rf_model.predict(X_train)
rf_test_pred = rf_model.predict(X_test)

# Decision Tree predictions
dt_train_pred = dt_model.predict(X_train)
dt_test_pred = dt_model.predict(X_test)

print("\n--- Random Forest ---")
print("Training accuracy:", accuracy_score(y_train, rf_train_pred))
print("Test accuracy:", accuracy_score(y_test, rf_test_pred))

print("\n--- Decision Tree ---")
print("Training accuracy:", accuracy_score(y_train, dt_train_pred))
print("Test accuracy:", accuracy_score(y_test, dt_test_pred))



importance = pd.Series(
    rf_model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nRandom Forest Feature Importance:")
print(importance)