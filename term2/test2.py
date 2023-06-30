import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA
import math

dry_bean = pd.read_csv("Dry_Bean.csv")

onehot_encoded_df = pd.get_dummies(dry_bean)

pca_model = PCA(n_components=2)
pca_model.fit(onehot_encoded_df)

df_2d = pd.DataFrame(pca_model.transform(onehot_encoded_df))


def kmeans(df, k, max_iteration=200):
    # df must be 2d with these columns : 0, 1
    def find_mean_of_points(points):
        for item in [point[0] for point in points]:
            if not isinstance(item , int) and not isinstance(item , float):
                print(item )
        
        for item in [point[1] for point in points]:
            if not isinstance(item , int) and not isinstance(item , float):
                print(item )
        
        return [
            np.mean([point[0] for point in points]),
            np.mean([point[1] for point in points]),
        ]

    def find_duplicates(array):
        results = []
        for index, i in enumerate(array):
            for index2, i2 in enumerate(array):
                if i2 == i and index != index2:
                    if not i in results:
                        results.append(i)
        return results

    x_values = df[0]
    y_values = df[1]
    points = [[x_values[i], y_values[i]] for i in range(len(x_values))]

    def calc_distance(point1, point2):
        return math.sqrt(
            abs(point2[0] - point1[0]) ** 2 + abs(point2[1] - point1[1]) ** 2
        )

    def find_nearest_centroid(centroids, point):
        distances = [calc_distance(point, centroid) for centroid in centroids]
        if len(find_duplicates(distances)) != 0:
            raise "Couldnt assign a centroid to a point : two centroids have the same distance with this point"
        index_of_max = distances.index(max(distances))
        return centroids[index_of_max]
    
    centroids = [
        np.random.choice(points)
        for i in range(k)
    ]

    """ instead of choice(x) -> [
        np.random.randint(min(x_values), max(x_values) + 1),
        np.random.randint(min(y_values), max(y_values) + 1),
    ] """
    plt.scatter(x_values, y_values, color="blue")
    plt.scatter(
        [centroid[0] for centroid in centroids],
        [centroid[1] for centroid in centroids],
        color="green",
    )

    for i in range(max_iteration):
        labeled_points = [
            {
                "point": point,
                "nearest_centroid": find_nearest_centroid(centroids, point),
            }
            for point in points
        ]

        plt.clf()
        plt.scatter(x_values, y_values, color="blue")
        prev_centroids = centroids.copy()

        centroids = []
        for centroid in prev_centroids:
            points_of_centroid = []
            for labeled_point in labeled_points:
                if labeled_point["nearest_centroid"] == centroid:
                    points_of_centroid.append(labeled_point["point"])
            centroids.append(find_mean_of_points(points_of_centroid))

        plt.scatter(
            list(map(lambda centroid: centroid[0], centroids)),
            list(map(lambda centroid: centroid[1], centroids)),
            color="green",
        )
        plt.pause(0.0001)
        if prev_centroids == centroids:
            break
    plt.show()


kmeans(df_2d, 3, max_iteration=10)
