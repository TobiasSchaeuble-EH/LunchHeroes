"""Tests for the distance module."""

import numpy as np

from lunchheros.distance import EuclideanDistance, MahattanDistance


def test_euclidean_distance():
    """Tests for the euclidean distance."""

    # make a vector of 3 dimensions
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    # calculate the euclidean distance
    dist = np.linalg.norm(a - b)
    # calculate the euclidean distance using the function
    dist_func = EuclideanDistance().calculate(a, b)

    assert dist == dist_func


def test_euclidean_distance_bool():
    """Tests for the euclidean distance."""

    # make a vector of 3 dimensions
    a = np.array([1, 0, 1])
    b = np.array([1, 0, 0])
    # calculate the euclidean distance
    dist = np.linalg.norm(a - b)
    # calculate the euclidean distance using the function
    dist_func = EuclideanDistance().calculate(a, b)

    assert dist == dist_func



def test_mahattan_distance():
    """Tests for the euclidean distance."""

    # make a vector of 3 dimensions
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    # calculate the euclidean distance
    dist = np.sum(np.abs(a - b))
    # calculate the euclidean distance using the function
    dist_func = MahattanDistance().calculate(a, b)

    assert dist == dist_func


def test_mahattan_distance_bool():
    """Tests for the euclidean distance."""

    # make a vector of 3 dimensions
    a = np.array([1, 0, 1])
    b = np.array([1, 0, 0])
    # calculate the euclidean distance
    dist = np.sum(np.abs(a - b))
    # calculate the euclidean distance using the function
    dist_func = MahattanDistance().calculate(a, b)

    assert dist == dist_func

