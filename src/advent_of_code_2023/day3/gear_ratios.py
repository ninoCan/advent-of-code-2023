from pathlib import Path

from advent_of_code_2023.day3.board import Board


def identify_and_sum_relevant_numbers(lines):
    board = Board(lines)


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    first_result = identify_and_sum_relevant_numbers(lines)
    print(first_result)
