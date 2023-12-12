import itertools
from dataclasses import dataclass
from typing import List, Self, Optional

import numpy as np

from src.advent_of_code_2023.day3.board import Board, Coords


@dataclass
class Universe:
    galaxies: List[Coords]
    board: Optional[Board] = None

    @classmethod
    def init_from_string_list(cls, content: List[str]) -> Self:
        new_board = Board(content)
        xs, ys = np.where(new_board.content == '#')
        return cls(
            galaxies=[Coords(x, y) for (x, y) in zip(xs, ys)],
            board=new_board,
        )

    @property
    def empty_rows(self):
        return [
            index
            for index, row in enumerate(self.board.content)
            if all([el == '.' for el in row])
        ]

    @property
    def empty_cols(self):
        return [
            index
            for index, col in enumerate(self.board.content.T)
            if all([el == '.' for el in col])
        ]

    @property
    def height(self) -> int:
        return self.board.height

    @property
    def width(self) -> int:
        return self.board.width

    @staticmethod
    def double_empty_indices(empty_indices: List[int]) -> List[int]:
        return list(
            itertools.chain(
                *[
                    [index + empty_index, index + empty_index + 1]
                    for index, empty_index in enumerate(empty_indices)
                ]
            )
        )

    def expand(self) -> "Universe":
        new_width = self.width + len(self.empty_cols)
        new_height = self.height + len(self.empty_rows)

        galaxies = [
            Coords(x_coord, y_coord)
            for x_coord in range(new_width)
            for y_coord in range(new_height)
            if (x_coord not in Universe.double_empty_indices(self.empty_rows))
            and (y_coord not in Universe.double_empty_indices(self.empty_cols))
        ]

        return Universe(galaxies=galaxies)
