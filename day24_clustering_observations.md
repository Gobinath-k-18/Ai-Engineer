
# Day 24 - Clustering Observations

## 1. What is clustering?
Clustering is an unsupervised machine learning technique that groups similar data points together based on their features.

## 2. Why is there no target label?
Clustering has no target label because we do not provide the correct answers to the model. We provide only input features, such as StudyHours and Attendance. The model discovers groups based on similarities in the data.

## 3. What is K-Means?
K-Means is an unsupervised machine learning algorithm that divides data into K clusters. It assigns each data point to the nearest centroid and repeatedly updates the centroids until the clusters stabilize or the stopping limit is reached.

## 4. What is a centroid?
A centroid is the center of a cluster. It is calculated by taking the average of the feature values of all data points assigned to that cluster.

## 5. What is inertia?
Inertia measures the sum of squared distances between data points and their assigned centroids. Lower inertia generally means the data points are closer to their centroids. However, inertia usually decreases when the number of clusters increases, so lower inertia alone does not determine the best K.

## 6. Elbow method
- K chosen for the example: 2
- What did I observe in the elbow plot?

The elbow method compares inertia for different values of K. I looked for the point where the inertia curve started flattening and adding more clusters provided smaller improvements. I used K = 2 as an example, but the elbow plot should be checked to decide whether it is a reasonable choice.

## 7. Cluster visualization
The scatter plot shows students grouped into different clusters based on StudyHours and Attendance. Points with the same cluster ID belong to the same group. The red X markers represent the centroids of the clusters.

## 8. Limitation
This is a tiny demonstration dataset with only 10 students. The clusters do not prove anything about real student performance. The results depend on the dataset, selected features, scaling, and number of clusters.
