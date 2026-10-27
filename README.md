# Day 27 — Fraud Detection Project

## 1. Problem Statement

The goal of this project is to build a machine learning classification system that identifies potentially fraudulent financial transactions.

The target column is `IsFraud`:
- `0` — Legitimate transaction
- `1` — Fraudulent transaction

Fraud detection is challenging because fraudulent transactions are often much less common than legitimate transactions. Therefore, precision, recall, and F1-score are important evaluation metrics.

## 2. Dataset

This project uses a small, synthetic dataset created for learning purposes.

- **Total transactions:** 20
- **Legitimate transactions:** 15 (75%)
- **Fraudulent transactions:** 5 (25%)
- **Original features:** TransactionAmount, TransactionsLastHour, AccountAgeDays, IsInternational
- **Target:** IsFraud

The dataset contains no missing values or duplicate rows.

## 3. Approach

### Data inspection and cleaning
- Inspected the dataset using Pandas.
- Checked for missing values and duplicate rows.
- Removed duplicate rows if present.

### Feature engineering
Created `AmountPerRecentTransaction` by dividing the transaction amount by the number of transactions in the last hour, with a minimum denominator of 1.

### Train-test split
- Training data: 15 transactions
- Testing data: 5 transactions
- Test size: 25%
- Random state: 42
- Stratified split to preserve class proportions as much as possible

### Machine learning models
Trained and compared:
1. Logistic Regression
2. Random Forest Classifier

Logistic Regression used StandardScaler in a pipeline. Both models used `class_weight="balanced"` to account for the class imbalance.

### Evaluation metrics
- Precision
- Recall
- F1-score
- Confusion matrix
- Average precision

Accuracy was also reported by the classification report, but it was not the only metric considered.

## 4. Results

Results from the five-transaction test set:

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Fraud precision | 0.50 | 1.00 |
| Fraud recall | 1.00 | 1.00 |
| Fraud F1-score | 0.667 | 1.00 |
| Average precision | 1.00 | 1.00 |
| Overall accuracy | 0.80 | 1.00 |

### Confusion matrices

**Logistic Regression**

```text
[[3 1]
 [0 1]]
```

**Random Forest**

```text
[[4 0]
 [0 1]]
```

On this particular test split, Random Forest classified all five transactions correctly. Logistic Regression detected the fraud case but incorrectly flagged one legitimate transaction.

## 5. Random Forest Feature Importance

The model reported the following feature importance values:

| Feature | Importance |
|---|---:|
| IsInternational | 0.23 |
| TransactionAmount | 0.22 |
| AmountPerRecentTransaction | 0.21 |
| TransactionsLastHour | 0.19 |
| AccountAgeDays | 0.15 |

These values describe how the trained Random Forest used features for its splits. They do not prove that a feature causes fraud or will be equally useful on other datasets.

## 6. Conclusion

Both models detected the single fraudulent transaction in the test set. Random Forest achieved higher fraud precision and F1-score on this split.

However, the dataset contains only 20 synthetic transactions and the test set contains only one fraud case. The results are too limited to establish reliable real-world performance or prove that one model is generally better.

Future improvements include using a larger, realistic dataset, evaluating on multiple splits or cross-validation folds, tuning classification thresholds, and monitoring precision-recall performance.

## 7. Technologies Used

- Python
- Pandas
- Scikit-learn
- Machine Learning Classification
- Feature Engineering
- Model Evaluation

## 8. How to Run

Install dependencies:

```bash
python -m pip install pandas scikit-learn
```

Run the project:

```bash
python day27_fraud_detection.py
```

**Note:** This is an educational project using synthetic data. It is not a production-ready fraud detection system.
