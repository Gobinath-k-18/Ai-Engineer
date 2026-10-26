
# Day 24: K-Means Clustering
# Topics: Clusters, Centroids, Inertia, Elbow Method

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# --------------------------------------------------
# 1. Create the dataset
# --------------------------------------------------

data = {
    "StudyHours": [1, 2, 2, 3, 4, 5, 6, 7, 8, 9],
    "Attendance": [50, 55, 58, 60, 70, 75, 82, 88, 92, 95]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# Input features only — no target column
X = df[["StudyHours", "Attendance"]]


# --------------------------------------------------
# 2. Scale the features
# --------------------------------------------------

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nScaled Features:")
print(X_scaled.round(2))


# --------------------------------------------------
# 3. Elbow Method: Calculate inertia for different K
# --------------------------------------------------

inertia_values = []
k_values = range(1, 7)

for k in k_values:
    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X_scaled)
    inertia_values.append(model.inertia_)

print("\nInertia Values:")
for k, inertia in zip(k_values, inertia_values):
    print(f"K = {k}, Inertia = {inertia:.2f}")


# --------------------------------------------------
# 4. Plot the Elbow Curve
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    list(k_values),
    inertia_values,
    marker="o"
)

plt.title("Elbow Method for K-Means")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.xticks(list(k_values))
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 5. Train the final K-Means model
# --------------------------------------------------

# Choose K = 2 as an example; inspect the elbow plot too.
best_k = 2

kmeans = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nClustered Dataset:")
print(df)


# --------------------------------------------------
# 6. Get the centroids
# --------------------------------------------------

# Convert centroids back to the original feature scales
centroids = scaler.inverse_transform(kmeans.cluster_centers_)

print("\nCluster Centroids:")
for i, center in enumerate(centroids):
    print(
        f"Cluster {i}: "
        f"Study Hours = {center[0]:.2f}, "
        f"Attendance = {center[1]:.2f}%"
    )


# --------------------------------------------------
# 7. Visualize the clusters
# --------------------------------------------------

plt.figure(figsize=(8, 5))

for cluster_id in sorted(df["Cluster"].unique()):
    cluster_data = df[df["Cluster"] == cluster_id]

    plt.scatter(
        cluster_data["StudyHours"],
        cluster_data["Attendance"],
        label=f"Cluster {cluster_id}",
        s=100
    )

# Plot centroid locations
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=250,
    color="red",
    edgecolors="black",
    label="Centroids"
)

plt.title("Student Groups Using K-Means")
plt.xlabel("Study Hours")
plt.ylabel("Attendance (%)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# 8. Final summary
# --------------------------------------------------

print("\nProject Summary")
print("----------------")
print(f"Number of students: {len(df)}")
print(f"Number of clusters: {best_k}")
print(f"Final model inertia: {kmeans.inertia_:.2f}")
print("Clustering completed successfully!")
