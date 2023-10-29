from sklearn.cluster import KMeans



def cluster(user_id, user_features, num_clusters):
    """Clusters the data points into ``num_clusters`` clusters.

    Args:
        user_id: list of users id
        user_features: list of users and their features
        num_clusters: The number of clusters to create.

    Returns:
        A list of cluster assignments. The i-th entry of the list is the cluster assignment of the i-th data point.
    """

    # Convert user_features list to a matrix
    user_matrix = np.array(user_features)

    # Create a k-means object with the desired number of clusters
    kmeans = KMeans(n_clusters=num_clusters)

    # Fit the k-means model to the data
    kmeans.fit(user_matrix)

    # Get the cluster labels assigned to each user
    cluster_labels = kmeans.labels_

    # Print the cluster labels assigned to each user
    for i in range(len(user_id)):
        print("User {} belongs to Cluster {}".format(user_id[i], cluster_labels[i]))

    return cluster_labels