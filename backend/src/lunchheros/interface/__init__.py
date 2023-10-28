"""Commonly used interfaces, used across different subpackages.

Note:
  - Subpackage-specific interfaces should be
    in a subpackage's version of such module.
  - This subpackage should not depend on other subpackages, so we
    do not introduce circular imports.
"""

from dataclasses import dataclass

from typing import Union


@dataclass
class Feature:
    value: Union[bool, int, float]


@dataclass
class Interest(Feature):
    value: bool
