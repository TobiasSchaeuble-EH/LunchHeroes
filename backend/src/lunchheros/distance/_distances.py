"""Implements Distance Classes"""

import lunchheros.interface as interface
import lunchheros.distance._interface as interface_distance

# import scikit-learn.metrics.pairwise as pairwise_metrics


class EuclideanDistances(interface_distance.Distance):
    """Ancestor-descendant similarity,
    adopted from @laurabquintas / Laura Quintas

    Counts the root as a mutation, i.e. considers pairs of ancestor-descendant nodes
    between root and nodes - effectivly making comparisons if mutations exist in
    both trees. May lead a higher similarity score than AncestorDescendantSimilarity.
    """

    def calculate(self, /, interst_val1: int, interst_val2: int) -> float:
        """Calculates similarity between ``tree1`` and ``tree2`` using `scphylo.tl.ad`.

        Args:
            tree1: root of the first tree. The nodes should be labeled with integers.
            tree2: root of the second tree. The nodes should be labeled with integers.

        Returns:
            similarity from ``tree1`` to ``tree2``
        """

        # return pairwise_metrics.euclidean_distances(interst_val1, interst_val2)
        return NotImplementedError

    def is_symmetric(self) -> bool:
        """Returns ``True`` if the similarity function is symmetric,
        i.e., :math:`s(t_1, t_2) = s(t_2, t_1)` for all pairs of users.

        Note:
            If it is not known whether the similarity function is symmetric,
            ``False`` should be returned.
        """
        return True
