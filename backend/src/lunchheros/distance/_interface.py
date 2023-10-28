"""Interfaces related to distance between user computations."""

from typing import Protocol, Union


class Distance(Protocol):
    """Interface for similarity or distance functions between the interests.

    The hyperparameters should be set
    at the class initialization stage,
    similarly as with models in SciKit-Learn.
    """

    def calculate(
        self,
        /,
        interest_val1: Union[bool, int, float],
        interest_val2: Union[bool, int, float],
    ) -> float:
        """Calculates distance between ``interest_val1`` and ``interest_val2``.

        Args:
            interest_val1: first interest value
            interest_val2: second interest value

        Returns:
            distance between ``interest_val1`` and ``interest_val2``
        """
        raise NotImplementedError

    def is_symmetric(self) -> bool:
        """Returns ``True`` if the distance function is symmetric,
        i.e., :math:`s(t_1, t_2) = s(t_2, t_1)` for all pairs of trees.

        Note:
            If it is not known whether the distance function is symmetric,
            ``False`` should be returned.
        """
        return False

    def triangle_inequality(self) -> bool:
        """Returns ``True`` if the triangle inequality

        .. math::

           d(t_1, t_3) <= d(t_1, t_2) + d(t_2, t_3)

        is known to hold for this distance.

        Note:
            If it is not known whether the triangle inequality
            holds for a metric, ``False`` should be returned.
        """
        return False
