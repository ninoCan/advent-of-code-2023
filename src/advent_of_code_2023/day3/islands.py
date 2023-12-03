from dataclasses import dataclass
from typing import List

import numpy as np

from advent_of_code_2023.day3.board import Board, Coords


@dataclass
class NumberIsland:
    value: int
    points: List[Coords]
    board: Board

    @property
    def has_neighboring_symbol(self) -> bool:
        neighboring_symbols = {
            self.board.get_neighbors_of_cell(*point.tuple).flatten()
            for point in self.points
            if not str.isdigit(self.board[*point.tuple])
        }
        return len(set) != 0


def cluster_coordinates_and_enumerate(
    points: List[Coords],
) -> List[List[Coords]]:
    """Return a list of lists where each list contains the coordinates of adjacent points"""
    clusters = []

    if not points:
        clusters.append([])
        return clusters

    current = points[0]
    current_cluster = [(0, current)]

    for index, point in enumerate(points[1:]):
        if are_adjacent(current, point):
            current_cluster.append((index + 1, point))
            current = point
        else:
            clusters.append(current_cluster)
            current_cluster = [(index + 1, point)]
            current = point
    else:
        clusters.append(current_cluster)

    return clusters


def are_adjacent(left: Coords, right: Coords) -> bool:
    return left.x == right.x and abs(left.y - right.y) == 1


def find_islands(board: Board) -> List[NumberIsland]:
    row_indices, col_indices = np.where(np.char.isdigit(board.content))
    digits = board.content[row_indices, col_indices]
    all_coordinates = list(zip(row_indices, col_indices))
    digits_and_coordinates = list(zip(digits, all_coordinates))
