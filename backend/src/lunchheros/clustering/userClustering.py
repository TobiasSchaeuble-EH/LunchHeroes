import numpy as np
from sklearn.cluster import DBSCAN
from scipy.spatial import distance

def generateUserClusters(distanceMatrix):
    """Generate clusters of users based on the distance matrix."""

    # Apply DBSCAN on the distance matrix
    dbscan = DBSCAN(metric='precomputed')
    clusters = dbscan.fit_predict(distanceMatrix)

    # clusters now contains the cluster labels for each user
    print(clusters)
