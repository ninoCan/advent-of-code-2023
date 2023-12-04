""""
Model a board with its content and methods
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple

import numpy as np


@dataclass
class Coords:
    x: int
    y: int

    @property
    def tuple(self) -> Tuple[int, int]:
        return self.x, self.y


class Board:
    def __init__(self, content: List[str]) -> None:
        self.height = len(content)
        self.width = len(content[0])
        self.content = np.char.array([[el for el in row] for row in content])

    def get(self, x: int, y: int) -> str:
        if x < self.height and y < self.width:
            return str(self.content[x, y])
        return ''

    def get_neighbors_of_cell(self, i: int, j: int) -> np.chararray:
        """Take the elements in a (at most) 3x3 slice centered around (x, y)"""
        coords = Coords(i, j)
        neighbors = [
            self.content[i, j]
            for i in range(max(0, coords.x - 1), min(self.height, coords.x + 2))
            for j in range(max(0, coords.y - 1), min(self.width, coords.y + 2))
            if (i, j) != coords.tuple
        ]
        return np.char.array(
            [char for char in neighbors if char not in {'.', ''}], unicode=True
        )
