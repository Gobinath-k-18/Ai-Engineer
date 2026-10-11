
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
