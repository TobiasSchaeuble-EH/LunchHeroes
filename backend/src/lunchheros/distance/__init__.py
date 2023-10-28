"""Subpackage related to calculation of distances between users."""

from lunchheros.distance._distances import EuclideanDistance, MahattanDistance

__all__ = ["EuclideanDistance",
           "MahattanDistance"]
