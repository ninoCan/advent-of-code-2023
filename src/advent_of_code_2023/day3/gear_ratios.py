import itertools
from pathlib import Path
from typing import List

from advent_of_code_2023.day3.board import Board
from advent_of_code_2023.day3.islands import find_islands, NumberIsland


def identify_and_sum_relevant_numbers(all_islands: List[NumberIsland]):
    valid_values = [
        island.value for island in all_islands if island.has_neighboring_symbol
    ]
    return sum(valid_values)


def identify_and_sum_true_gears(all_islands: List[NumberIsland]):
    islands_with_asterisk = [
        island for island in all_islands if '*' in set(island.adjacent_symbols)
    ]
    gear_ratios = [
        left.value * right.value
        for left, right in itertools.combinations(islands_with_asterisk, r=2)
        if left.gear_position == right.gear_position
    ]
    return sum(gear_ratios)


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    board = Board(lines)
    all_part_numbers = find_islands(board)
    first_result = identify_and_sum_relevant_numbers(all_part_numbers)
    second_result = identify_and_sum_true_gears(all_part_numbers)
    print(second_result)
