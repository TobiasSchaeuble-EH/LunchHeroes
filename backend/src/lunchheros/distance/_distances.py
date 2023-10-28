"""Implements Distance Classes"""

import lunchheros.distance._interface as interface_distance

import sklearn.metrics as metrics


class EuclideanDistance(interface_distance.Distance):
    """Euclidean distance between two interests."""

    def calculate(self, /, interst_vec1, interst_vec2) -> float:
        """Calculates distance between ``interst_val1`` and ``interst_val2``."""

        return metrics.pairwise.euclidean_distances([interst_vec1], [interst_vec2])

    def is_symmetric(self) -> bool:
        """Returns ``True`` if the similarity function is symmetric,
        i.e., :math:`s(t_1, t_2) = s(t_2, t_1)` for all pairs of users.

        Note:
            If it is not known whether the similarity function is symmetric,
            ``False`` should be returned.
        """
        return True
    
class MahattanDistance(interface_distance.Distance):
    """Manhattan distance between two interests."""

    def calculate(self, /, interst_vec1, interst_vec2) -> float:
        """Calculates distance between ``interst_val1`` and ``interst_val2``."""

        return metrics.pairwise.manhattan_distances([interst_vec1], [interst_vec2])

    def is_symmetric(self) -> bool:
        """Returns ``True`` if the similarity function is symmetric,
        i.e., :math:`s(t_1, t_2) = s(t_2, t_1)` for all pairs of users.

        Note:
            If it is not known whether the similarity function is symmetric,
            ``False`` should be returned.
        """
        return True
    