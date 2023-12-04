from dataclasses import dataclass
from typing import List, Tuple

import numpy as np

from advent_of_code_2023.day3.board import Board, Coords


@dataclass
class NumberIsland:
    value: int
    points: List[Coords]
    board: Board

    @property
    def adjacent_symbols(self) -> List[str]:
        all_neighbors = [
            self.board.get_neighbors_of_cell(*point.tuple)
            for point in self.points
        ]

        return [
            item
            for sublist in all_neighbors
            for item in sublist
            if not str.isdigit(item)
        ]

    @property
    def has_neighboring_symbol(self) -> bool:
        return len(self.adjacent_symbols) != 0


def cluster_coordinates_and_enumerate(
    points: List[Coords],
) -> List[List[Tuple[int, Coords]]]:
    """Return a list of lists where each list contains the coordinates of adjacent points"""
    if not points:
        return [[]]

    clusters = []
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
    all_digits = board.content[row_indices, col_indices]
    all_coordinates = [Coords(*x_y) for x_y in zip(row_indices, col_indices)]

    clustered_values = assemble_value_points_pair_cluster(
        all_digits, all_coordinates
    )

    return instantiate_NumberIsland_list(board, clustered_values)


def instantiate_NumberIsland_list(board, clustered_values):
    islands = []
    for cluster in clustered_values:
        points = [coord for _, coord in cluster]
        digits = [digit for digit, _ in cluster]
        value = int("".join(digits))
        islands.append(NumberIsland(value, points, board))
    return islands


def assemble_value_points_pair_cluster(all_digits, all_coordinates):
    indexed_coord_clusters = cluster_coordinates_and_enumerate(all_coordinates)
    return [
        [(all_digits[index], point) for (index, point) in cluster]
        for cluster in indexed_coord_clusters
    ]
