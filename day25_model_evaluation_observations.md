# Day 25 - Model Evaluation Observations

## 1. What are TP, TN, FP and FN?

These terms describe the four possible outcomes of a binary classification model.

- **TP (True Positive):** The actual class is positive, and the model predicts positive.
- **TN (True Negative):** The actual class is negative, and the model predicts negative.
- **FP (False Positive):** The actual class is negative, but the model predicts positive.
- **FN (False Negative):** The actual class is positive, but the model predicts negative.

Example: If Pass is the positive class, predicting Pass for a student who actually failed is a False Positive.

## 2. Difference between precision and recall

- **Precision:** Out of all the positive predictions made by the model, how many were actually positive?
- **Recall:** Out of all the actual positive cases, how many did the model correctly identify?

Precision is useful when false positives are costly. Recall is important when missing positive cases is costly.

## 3. What does ROC-AUC measure?

ROC-AUC stands for Receiver Operating Characteristic — Area Under the Curve.

It measures how well a classification model distinguishes between positive and negative classes across different prediction thresholds.

- AUC = 1.0 indicates perfect ranking.
- AUC = 0.5 indicates random-ranking-level performance.
- AUC below 0.5 can indicate that the model tends to rank the classes in the wrong direction.

ROC-AUC evaluates ranking ability and does not guarantee good predictions at every chosen threshold.

## 4. Difference between MAE, MSE, RMSE and R²

These metrics are used to evaluate regression models.

- **MAE (Mean Absolute Error):** The average absolute difference between actual and predicted values.
- **MSE (Mean Squared Error):** The average squared difference between actual and predicted values. Large errors receive more weight.
- **RMSE (Root Mean Squared Error):** The square root of MSE. It expresses error in the same units as the target.
- **R² (R-squared):** Measures model fit relative to a baseline that predicts the mean of the actual target values. It can be negative if the model performs worse than that baseline.

Generally, lower MAE, MSE and RMSE indicate smaller errors. Higher R² is generally better when evaluating models on the same dataset.

## 5. Why can accuracy be misleading with imbalanced classes?

Accuracy measures the proportion of all predictions that are correct. It can look high when one class is much more common than another.

For example, suppose a dataset contains 95 Fail cases and 5 Pass cases. A model that predicts Fail for every case achieves 95% accuracy but misses every Pass case.

In this situation, accuracy alone does not show the model's weakness. We should also examine the confusion matrix, precision, recall and F1-score.

## 6. Key learning

Model evaluation helps us understand a model's strengths and weaknesses. We should choose metrics based on the problem, the class distribution and the cost of different prediction errors rather than relying on a single score.