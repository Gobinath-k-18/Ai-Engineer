
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import (
    StandardScaler,
    MinMaxScaler,
    OneHotEncoder
)
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# --------------------------------------------------
# 1. CREATE THE DATASET
# --------------------------------------------------

data = {
    "StudyHours": [
        1, 2, 2, 3, 4, 5, 6, 7, 8, 9,
        2, 4, 6, 8, 3, 7, 5, 9, 1, 6
    ],
    "Attendance": [
        60, 65, 70, 72, 75, 80, 85, 88, 92, 95,
        62, 74, 84, 96, 71, 90, 78, 94, 58, 86
    ],
    "StudyMode": [
        "Online", "Offline", "Online", "Offline", "Online",
        "Offline", "Online", "Offline", "Online", "Offline",
        "Online", "Offline", "Online", "Offline", "Online",
        "Offline", "Online", "Offline", "Online", "Offline"
    ],
    "Pass": [
        0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
        0, 1, 1, 1, 0, 1, 1, 1, 0, 1
    ]
}

df = pd.DataFrame(data)

print("FULL DATASET")
print(df.head())
print("\nDataset shape:", df.shape)


# --------------------------------------------------
# 2. SEPARATE FEATURES AND TARGET
# --------------------------------------------------

X = df[["StudyHours", "Attendance", "StudyMode"]]
y = df["Pass"]

print("\nFeatures shape:", X.shape)
print("Target shape:", y.shape)


# --------------------------------------------------
# 3. SPLIT DATA BEFORE PREPROCESSING
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))


# --------------------------------------------------
# 4. CHOOSE A NUMERICAL SCALER
# --------------------------------------------------

# Choose either "standard" or "minmax".
SCALER_CHOICE = "standard"

if SCALER_CHOICE == "standard":
    numerical_scaler = StandardScaler()
elif SCALER_CHOICE == "minmax":
    numerical_scaler = MinMaxScaler()
else:
    raise ValueError(
        "SCALER_CHOICE must be 'standard' or 'minmax'"
    )


# --------------------------------------------------
# 5. PREPROCESS NUMERICAL AND CATEGORICAL FEATURES
# --------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            numerical_scaler,
            ["StudyHours", "Attendance"]
        ),
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            ["StudyMode"]
        )
    ]
)


# --------------------------------------------------
# 6. BUILD THE PIPELINE
# --------------------------------------------------

model = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        (
            "feature_selection",
            SelectKBest(score_func=f_classif, k=3)
        ),
        (
            "classifier",
            LogisticRegression(max_iter=1000)
        )
    ]
)


# --------------------------------------------------
# 7. TRAIN THE MODEL
# --------------------------------------------------

model.fit(X_train, y_train)

print("\nModel training completed!")


# --------------------------------------------------
# 8. MAKE TEST PREDICTIONS
# --------------------------------------------------

y_pred = model.predict(X_test)

print("\nActual values:")
print(y_test.to_list())

print("\nPredicted values:")
print(y_pred.tolist())


# --------------------------------------------------
# 9. EVALUATE THE MODEL
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy, 3))

print("\nClassification report:")
print(
    classification_report(
        y_test,
        y_pred,
        zero_division=0
    )
)


# --------------------------------------------------
# 10. PREDICT FOR A NEW STUDENT
# --------------------------------------------------

new_student = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "StudyMode": ["Online"]
})

new_prediction = model.predict(new_student)

print("\nNew student details:")
print(new_student)

if new_prediction[0] == 1:
    print("Prediction: Student may PASS")
else:
    print("Prediction: Student may FAIL")


# --------------------------------------------------
# 11. SHOW SELECTED FEATURES
# --------------------------------------------------

selected_features = (
    model.named_steps["feature_selection"]
    .get_support()
)

all_feature_names = (
    model.named_steps["preprocessing"]
    .get_feature_names_out()
)

print("\nAll preprocessed feature names:")
print(all_feature_names.tolist())

print("\nSelected features:")
print(all_feature_names[selected_features].tolist())


# --------------------------------------------------
# 12. EXPLAIN THE SCALER OPTIONS
# --------------------------------------------------

print("\nScaler used:", SCALER_CHOICE)
print("Preprocessing and feature selection are inside the pipeline.")
print("The pipeline is fitted using training data only.")
