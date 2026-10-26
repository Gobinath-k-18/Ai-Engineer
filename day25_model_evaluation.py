
# Day 25 - Model Evaluation
# Topics:
# Confusion Matrix, Accuracy, Precision, Recall, F1-score,
# ROC-AUC, MAE, MSE, RMSE, R2, and misleading accuracy.

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# ==================================================
# PART 1: CLASSIFICATION METRICS
# ==================================================

print("=" * 50)
print("PART 1: CLASSIFICATION METRICS")
print("=" * 50)

# Actual results: 1 = Pass, 0 = Fail
y_actual = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# Predictions made by the model
y_predicted = [1, 1, 1, 0, 0, 0, 0, 0, 0, 1]

# Model's predicted probability of Pass (class 1)
y_probabilities = [
    0.95, 0.85, 0.70, 0.40, 0.30,
    0.20, 0.10, 0.15, 0.25, 0.65
]

# Confusion matrix
cm = confusion_matrix(y_actual, y_predicted, labels=[0, 1])

print("\nConfusion Matrix (rows = actual, columns = predicted):")
print(cm)

# Extract TN, FP, FN, TP for labels [0, 1]
tn, fp, fn, tp = cm.ravel()

print(f"\nTrue Negatives (TN): {tn}")
print(f"False Positives (FP): {fp}")
print(f"False Negatives (FN): {fn}")
print(f"True Positives (TP): {tp}")

# Classification metrics
accuracy = accuracy_score(y_actual, y_predicted)
precision = precision_score(y_actual, y_predicted, zero_division=0)
recall = recall_score(y_actual, y_predicted, zero_division=0)
f1 = f1_score(y_actual, y_predicted, zero_division=0)
roc_auc = roc_auc_score(y_actual, y_probabilities)

print("\nClassification Scores:")
print(f"Accuracy : {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall   : {recall:.3f}")
print(f"F1-score : {f1:.3f}")
print(f"ROC-AUC  : {roc_auc:.3f}")

print("\nClassification Report:")
print(classification_report(
    y_actual,
    y_predicted,
    target_names=["Fail (0)", "Pass (1)"],
    zero_division=0
))


# ==================================================
# PART 2: REGRESSION METRICS
# ==================================================

print("\n" + "=" * 50)
print("PART 2: REGRESSION METRICS")
print("=" * 50)

# Actual house prices in lakhs
y_reg_actual = [10, 20, 30, 40]

# Predicted house prices in lakhs
y_reg_predicted = [12, 18, 33, 39]

# Calculate metrics
mae = mean_absolute_error(y_reg_actual, y_reg_predicted)
mse = mean_squared_error(y_reg_actual, y_reg_predicted)
rmse = mse ** 0.5
r2 = r2_score(y_reg_actual, y_reg_predicted)

print("\nActual Prices     :", y_reg_actual)
print("Predicted Prices  :", y_reg_predicted)

print("\nRegression Scores:")
print(f"MAE  : {mae:.3f} lakhs")
print(f"MSE  : {mse:.3f} lakhs squared")
print(f"RMSE : {rmse:.3f} lakhs")
print(f"R2   : {r2:.3f}")


# ==================================================
# PART 3: WHEN ACCURACY IS MISLEADING
# ==================================================

print("\n" + "=" * 50)
print("PART 3: WHEN ACCURACY IS MISLEADING")
print("=" * 50)

# Imagine 100 cases:
# 95 are negative (Fail), and 5 are positive (Pass).
# The model predicts negative for every case.

y_imbalanced_actual = [0] * 95 + [1] * 5
y_imbalanced_predicted = [0] * 100

imbalanced_accuracy = accuracy_score(
    y_imbalanced_actual,
    y_imbalanced_predicted
)

imbalanced_precision = precision_score(
    y_imbalanced_actual,
    y_imbalanced_predicted,
    zero_division=0
)

imbalanced_recall = recall_score(
    y_imbalanced_actual,
    y_imbalanced_predicted,
    zero_division=0
)

imbalanced_f1 = f1_score(
    y_imbalanced_actual,
    y_imbalanced_predicted,
    zero_division=0
)

print("\nActual class counts:")
print("Fail (0): 95")
print("Pass (1): 5")

print("\nModel predicts Fail for every case.")

print("\nConfusion Matrix:")
print(confusion_matrix(
    y_imbalanced_actual,
    y_imbalanced_predicted,
    labels=[0, 1]
))

print("\nMetrics:")
print(f"Accuracy : {imbalanced_accuracy:.3f}")
print(f"Precision: {imbalanced_precision:.3f}")
print(f"Recall   : {imbalanced_recall:.3f}")
print(f"F1-score : {imbalanced_f1:.3f}")

print("\nLesson:")
print("Accuracy alone can be misleading with imbalanced classes.")
print("Always check the confusion matrix and suitable class metrics.")

print("\nDay 25 Model Evaluation completed successfully!")
