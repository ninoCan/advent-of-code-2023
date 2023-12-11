from typing import List

import numpy as np

from src.advent_of_code_2023.day3.board import Coords, Board


class PipeCoords(Coords):
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value: str = value


class PipeBoard(Board):
    def __init__(self, content: List[str]):
        super().__init__(content)
        start_position = np.where(self.content == 'S')
        self.start_position = Coords(
            int(start_position[0][0]), int(start_position[1][0])
        )

    def get_following_neighbor_pipes(
        self, current: PipeCoords
    ) -> List[PipeCoords]:
        x, y = current.tuple
        north_pieces = "|7F"
        south_pieces = "|LJ"
        west_pieces = "-FL"
        east_pieces = "-7J"
        good_neighbors = []
        north, south = x - 1, x + 1
        west, east = y - 1, y + 1
        if (value := self.get(north, y)) in north_pieces:
            good_neighbors.append(PipeCoords(north, y, value))
        if (value := self.get(south, y)) in south_pieces:
            good_neighbors.append(PipeCoords(south, y, value))
        if (value := self.get(x, west)) in west_pieces:
            good_neighbors.append(PipeCoords(x, west, value))
        if (value := self.get(x, east)) in east_pieces:
            good_neighbors.append(PipeCoords(x, east, value))
        return good_neighbors
