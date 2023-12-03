from pathlib import Path

from advent_of_code_2023.day3.board import Board
from advent_of_code_2023.day3.islands import find_islands


def identify_and_sum_relevant_numbers(input_lines):
    board = Board(input_lines)
    all_island = find_islands(board)
    valid_islands = [
        island for island in all_island if island.has_neighboring_symbol
    ]
    return sum([island.value for island in valid_islands])


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    first_result = identify_and_sum_relevant_numbers(lines)
    print(first_result)
