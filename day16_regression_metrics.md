# Day 16 - Regression Concepts

## What is Regression?

Regression is a supervised machine learning technique used to predict numerical values.

Examples:
- House price
- Student marks
- Salary
- Temperature

---

## Linear Regression

Linear Regression finds a relationship between input features and a numerical target using a line.

Basic equation:

y = mx + b

Where:
- x = input feature
- y = predicted target
- m = slope
- b = intercept

Example:

Study Hours → Marks

The model learns the relationship between study hours and marks and uses it to predict marks for new students.

---

## Cost Function

A cost function measures how wrong the model's predictions are.

- Lower cost generally means better predictions.
- Linear regression commonly uses Mean Squared Error as a cost function.

---

## Gradient Descent

Gradient Descent is an optimization method used to minimize the cost function.

Basic idea:

High Cost
↓
Adjust model parameters
↓
Calculate cost again
↓
Continue reducing cost
↓
Lower Cost

---

## MAE - Mean Absolute Error

MAE is the average absolute difference between actual and predicted values.

MAE = average(|actual - predicted|)

Example:

Actual:  [80, 60, 90]
Predicted: [75, 65, 85]

Errors: [5, -5, 5]

Absolute errors: [5, 5, 5]

MAE = 5

Lower MAE is generally better.

---

## MSE - Mean Squared Error

MSE is the average of squared prediction errors.

MSE = average((actual - predicted)^2)

MSE gives more importance to larger errors because the errors are squared.

Lower MSE is generally better.

---

## RMSE - Root Mean Squared Error

RMSE is the square root of MSE.

RMSE = √MSE

RMSE is expressed in the same units as the target.

For example, when predicting marks, RMSE is in marks.

Lower RMSE is generally better.

---

## R² - R-squared

R² tells us how much of the variation in the target is explained by the regression model.

For example:

R² = 0.90

means the model explains about 90% of the variation in the target on the evaluated data.

R² should not be interpreted as "90% accuracy."

Higher R² is generally better.

---

## Metric Summary

| Metric | Meaning | Better |
|---|---|---|
| MAE | Average absolute error | Lower |
| MSE | Average squared error | Lower |
| RMSE | Square root of MSE | Lower |
| R² | Variation explained by model | Higher |

---

## Scikit-learn Workflow

The basic regression workflow is:

1. Prepare the dataset
2. Separate X and y
3. Split training and testing data
4. Create the model
5. Train using `.fit()`
6. Predict using `.predict()`
7. Evaluate using regression metrics

Example:

```python
model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)