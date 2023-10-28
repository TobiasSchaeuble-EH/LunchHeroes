"""Subpackage related to calculation of distances between users."""

from lunchheros.distance._distances import EuclideanDistance, MahattanDistance

from lunchheros.distance._utils import calculate_distance_matrix

__all__ = ["EuclideanDistance", "MahattanDistance", "calculate_distance_matrix"]
