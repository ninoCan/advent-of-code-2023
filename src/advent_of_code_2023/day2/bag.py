"""
This module contains the modelling of the bag and the functions acting on it.
"""
from __future__ import annotations

from dataclasses import dataclass, fields


@dataclass
class Bag:
    red: int = 0
    green: int = 0
    blue: int = 0

    def satisfy_constraint(self, constraint: Bag) -> bool:
        all_attrs = fields(self)
        return all(
            getattr(self, field.name) <= getattr(constraint, field.name)
            for field in all_attrs
        )

    @classmethod
    def init_from_string(cls, match_string: str) -> Bag:
        """Parse a match string and return a Bag object"""
        match_values = {
            color: int(quantity)
            for quantity_color in match_string.split(", ")
            for quantity, color in [quantity_color.split()]
        }
        return cls(**match_values)
