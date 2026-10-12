# Day 21 — Random Forest

## 1. Objective
Train a Random Forest classifier and compare its performance with a Decision Tree classifier.

## 2. Dataset
- Total rows: 10
- Features: `StudyHours`, `Attendance`
- Target: `Pass`
- Training rows: 8
- Testing rows: 2

## 3. Model Comparison

| Metric | Random Forest | Decision Tree |
|---|---:|---:|
| Training Accuracy | 100% | 100% |
| Test Accuracy | 100% | 100% |

Both models correctly predicted the two test examples in this experiment.

**Limitation:** The dataset is very small. Two test examples are not enough to conclude that either model will perform well on new, real-world data.

## 4. Random Forest Feature Importance

Add the actual values printed by Python:

- `StudyHours`: [enter actual value]
- `Attendance`: [enter actual value]

The feature with the higher importance value contributed more to the model's tree-splitting decisions. Feature importance does not prove causation.

## 5. What I Learned
- Ensemble learning combines multiple models.
- Bagging trains models on bootstrap samples.
- Random Forest combines multiple Decision Trees and considers random subsets of features when splitting.
- `n_estimators` controls the number of trees.
- `feature_importances_` provides feature importance scores.
- Training accuracy and test accuracy measure performance on different datasets.

