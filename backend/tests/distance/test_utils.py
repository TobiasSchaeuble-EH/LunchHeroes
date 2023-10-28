"""Tests for the distance module."""

import numpy as np

from lunchheros.distance._utils import calculate_distance_matrix
from lunchheros.distance import ManhattanDistance


def test_calculate_distance_matrix():
    """Tests for the calculate_distance_matrix function."""

    # make 3 vectors of length 4
    a = np.array([1, 2, 3, 4])
    b = np.array([4, 5, 6, 7])
    c = np.array([7, 8, 9, 10])
    # make a list of the vectors
    users = [a, b, c]
    # calculate the euclidean distance for all pairs of vectors
    dist = np.zeros((3, 3))
    for i, vec1 in enumerate(users):
        for j, vec2 in enumerate(users):
            dist[i, j] = np.sum(np.abs(vec1 - vec2))
    # calculate the manhattan distance using the function
    dist2 = calculate_distance_matrix(users, distance=ManhattanDistance)

    print(dist)
    print(dist2)
    assert np.allclose(dist, dist2)
