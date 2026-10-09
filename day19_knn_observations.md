# Day 19 — K-Nearest Neighbors (KNN)

## What I learned

- KNN predicts using the nearest data points.
- Distance measures how close data points are.
- K controls how many neighbors are considered.
- KNN classification predicts categories.
- KNN regression predicts numerical values.
- Feature scaling makes numerical features comparable.

## Experiment

I trained KNN classification models using K = 1, 3, and 5.

I compared models with and without StandardScaler.

## Results

| K | Accuracy without scaling | Accuracy with scaling |
|---|---|---|
| 1 | 100% | 100% |
| 3 | 100% | 100% |
| 5 | 100% | 100% |

## Observations

1. All three K values predicted both test students correctly.
2. Scaling did not change the predictions in this dataset.
3. The dataset has only 10 students, with 2 used for testing.
4. The accuracy result is based on just 2 test examples, so it does not prove general performance.
5. More data and further testing are needed to assess reliability.

## Conclusion

KNN uses distances to make predictions. Feature scaling can affect distances and may change predictions on other datasets. The best K value should be selected through appropriate evaluation.