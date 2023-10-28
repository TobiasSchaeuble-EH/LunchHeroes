"""Temporarily existing module with utility functions.

When the structure of the subpackage starts to appear,
we will move the functions here to the right packages.

Note:
    Treat this submodule as a part of the *private* API.
"""

from lunchheros.distance._interface import Distance

import numpy as np


def calculate_distance_matrix(
    users: list[list],
    *,
    distance: Distance,
) -> np.ndarray:
    """Calculates a cross-distance matrix
    ``d[i, j] = distance(trees1[i], trees2[j])``

    Args:
        vec1: sequence of trees in one set, length m
        vec1: sequence of trees in the second set, length n
        distance: distance or similarity function

    Returns:
        distance matrix, shape (m, n)
    """
    m, n = len(users), len(users)

    result = np.zeros((m, n))

    for i, vec1 in enumerate(users):
        for j, vec2 in enumerate(users):
            result[i, j] = distance().calculate(vec1, vec2)
        # print(f"Distance between user {i} and {j} is {result[i, j]}")

    return result
