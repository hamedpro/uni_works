import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

# Question 4)))))

# Set the random seed for reproducibility
np.random.seed(42)

# Read in the dataset and perform one-hot encoding
df = pd.read_csv("Dry_Bean.csv")
onehot_encoded_df = pd.get_dummies(df)


# Use PCA to reduce the dimensionality of the dataset to 2 features
pca_model = pd.DataFrame(PCA(n_components=2).fit_transform(onehot_encoded_df))


# Define the k-means clustering function
def kmeans(X, k, epsilon=1e-5):
    centroids = X[np.random.choice(len(X), k, replace=False)]
    fig, ax = plt.subplots()
    counter = 0
    prev_clusters = np.zeros(X.shape[0])
    while True:
        # Assign each data point to the nearest centroid
        clusters = np.argmin(
            np.linalg.norm(X[:, np.newaxis] - centroids, axis=2), axis=1
        )
        # Update the position of the centroids
        new_centroids = np.array([X[clusters == j].mean(axis=0) for j in range(k)])
        # Check for convergence
        if np.allclose(centroids, new_centroids, rtol=epsilon):
            break
        if np.array_equal(prev_clusters, clusters):
            counter += 1
            if counter == 5:
                break
        else:
            prev_clusters = clusters
            counter = 0
        centroids = new_centroids
        ax.clear()
        ax.scatter(X[:, 0], X[:, 1], c=clusters)
        ax.scatter(
            centroids[:, 0],
            centroids[:, 1],
            marker="o",
            s=50,
            edgecolors="black",
            linewidths=2,
            c="#050505",
        )
        plt.pause(0.1)
    plt.show()


# Call the k-means clustering function
kmeans(pca_model.values, k=5)
