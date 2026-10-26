# Day 26 — ML Preprocessing Observations

## 1. Train/Test Split

I split the dataset into training and testing sets before fitting any preprocessing steps.

- `test_size=0.25` reserves 25% of the data for testing.
- `random_state=42` makes the split reproducible.
- `stratify=y` helps preserve the Pass/Fail class proportions.

**Observation:** The model learns from training data and is evaluated on unseen test data.

## 2. StandardScaler vs MinMaxScaler

### StandardScaler
- Transforms numerical features to have approximately mean 0 and standard deviation 1.
- Useful for algorithms such as Logistic Regression, SVM, and KNN.

### MinMaxScaler
- Usually scales numerical features to the range 0 to 1.
- The resulting values can be sensitive to outliers.

**Observation:** Both methods scale numerical features, but they use different approaches. The better choice depends on the data and model.

In my script, I can switch between the scalers using `SCALER_CHOICE`.

## 3. OneHotEncoder

I used `OneHotEncoder(handle_unknown="ignore")` to convert the categorical `StudyMode` feature into numerical columns.

For example:

| StudyMode | Online | Offline |
|---|---:|---:|
| Online | 1 | 0 |
| Offline | 0 | 1 |

**Observation:** Encoding allows the model to process categorical features numerically. Unknown categories can be handled during transformation without raising an error.

## 4. Feature Selection

I used:

`SelectKBest(score_func=f_classif, k=3)`

- `f_classif` scores features using an ANOVA F-test for classification.
- `k=3` selects the three highest-scoring features.
- Feature selection is fitted using training data and training labels.

**Observation:** Feature selection reduces the number of inputs given to the classifier. It does not guarantee better model performance.

## 5. Pipeline

I created a pipeline containing:

1. `ColumnTransformer` for numerical scaling and categorical encoding.
2. `SelectKBest` for feature selection.
3. `LogisticRegression` for classification.

**Observation:** The pipeline keeps preprocessing, feature selection, and model training in one workflow. When fitted on training data, these steps learn from training data only.

## 6. Preventing Data Leakage

I used this workflow:

1. Separate features (`X`) and target (`y`).
2. Split the data into training and testing sets.
3. Fit the pipeline using `X_train` and `y_train`.
4. Predict on `X_test` using the fitted pipeline.
5. Evaluate predictions against `y_test`.

**Observation:** This prevents the preprocessing steps from learning parameters or selecting features using the test set.

For cross-validation, the complete pipeline should also be evaluated within each training fold.

## 7. Model Results

- **Model:** Logistic Regression
- **Dataset:** 20 sample student records
- **Test size:** 25%
- **Scaler tested:** [Fill in StandardScaler, MinMaxScaler, or both]
- **Accuracy