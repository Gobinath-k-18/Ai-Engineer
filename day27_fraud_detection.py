
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    average_precision_score
)

# ==========================================
# 1. CREATE THE DATASET
# ==========================================

data = {
    "TransactionAmount": [
        100, 250, 80, 1200, 75,
        5000, 150, 90, 3200, 60,
        700, 15000, 200, 4500, 50,
        900, 180, 8000, 125, 600
    ],
    "TransactionsLastHour": [
        1, 2, 1, 4, 1,
        9, 2, 1, 7, 1,
        3, 12, 2, 8, 1,
        4, 2, 10, 1, 3
    ],
    "AccountAgeDays": [
        900, 600, 1200, 300, 1500,
        20, 800, 1100, 45, 1300,
        400, 10, 700, 30, 1600,
        250, 850, 15, 1000, 500
    ],
    "IsInternational": [
        0, 0, 0, 1, 0,
        1, 0, 0, 1, 0,
        0, 1, 0, 1, 0,
        0, 0, 1, 0, 0
    ],
    "IsFraud": [
        0, 0, 0, 0, 0,
        1, 0, 0, 1, 0,
        0, 1, 0, 1, 0,
        0, 0, 1, 0, 0
    ]
}

df = pd.DataFrame(data)

# ==========================================
# 2. INSPECT AND CLEAN THE DATA
# ==========================================

print("=" * 50)
print("FRAUD DETECTION PROJECT")
print("=" * 50)

print("\nFirst five transactions:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

# Remove duplicate rows if any exist
df = df.drop_duplicates().copy()

print("\nFraud class counts:")
print(df["IsFraud"].value_counts())

print("\nFraud class proportions:")
print(df["IsFraud"].value_counts(normalize=True))

# ==========================================
# 3. FEATURE ENGINEERING
# ==========================================

df["AmountPerRecentTransaction"] = (
    df["TransactionAmount"]
    / df["TransactionsLastHour"].clip(lower=1)
)

print("\nDataset with engineered feature:")
print(df.head())

# ==========================================
# 4. SPLIT FEATURES AND TARGET
# ==========================================

X = df.drop(columns=["IsFraud"])
y = df["IsFraud"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))

print("\nTraining class counts:")
print(y_train.value_counts())

print("\nTesting class counts:")
print(y_test.value_counts())

# ==========================================
# 5. CREATE THE MODELS
# ==========================================

models = {
    "Logistic Regression": make_pipeline(
        StandardScaler(),
        LogisticRegression(
            class_weight="balanced",
            random_state=42
        )
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        class_weight="balanced",
        random_state=42
    )
}

# ==========================================
# 6. TRAIN AND EVALUATE THE MODELS
# ==========================================

results = []

for name, model in models.items():

    # Train the model
    model.fit(X_train, y_train)

    # Predict fraud labels
    predictions = model.predict(X_test)

    # Get probability of fraud
    probabilities = model.predict_proba(X_test)[:, 1]

    # Confusion matrix
    cm = confusion_matrix(
        y_test,
        predictions,
        labels=[0, 1]
    )

    # Classification report
    report = classification_report(
        y_test,
        predictions,
        labels=[0, 1],
        target_names=["Legitimate", "Fraud"],
        zero_division=0,
        output_dict=True
    )

    # Average precision
    avg_precision = average_precision_score(
        y_test,
        probabilities
    )

    fraud_precision = report["Fraud"]["precision"]
    fraud_recall = report["Fraud"]["recall"]
    fraud_f1 = report["Fraud"]["f1-score"]

    results.append({
        "Model": name,
        "Fraud Precision": fraud_precision,
        "Fraud Recall": fraud_recall,
        "Fraud F1": fraud_f1,
        "Average Precision": avg_precision
    })

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    print("\nConfusion matrix:")
    print(cm)

    print("\nClassification report:")
    print(classification_report(
        y_test,
        predictions,
        labels=[0, 1],
        target_names=["Legitimate", "Fraud"],
        zero_division=0
    ))

    print("Fraud average precision:", round(avg_precision, 3))

# ==========================================
# 7. COMPARE THE MODELS
# ==========================================

results_df = pd.DataFrame(results)

print("\n" + "=" * 50)
print("MODEL COMPARISON")
print("=" * 50)

print(results_df.round(3).to_string(index=False))

# ==========================================
# 8. FEATURE IMPORTANCE
# ==========================================

rf_model = models["Random Forest"]

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
}).sort_values(
    by="Importance",
    ascending=False
)

print("\nRandom Forest feature importance:")
print(importance_df.to_string(index=False))

print("\nProject completed!")
