import itertools
from pathlib import Path
from typing import List

from src.advent_of_code_2023.day5.seed_to_location import parse_digits


def assemble_triangle(sequence: List[int]) -> List[List[int]]:
    triangle, prev = [sequence], sequence
    while not all([item == 0 for item in prev]):
        couples = itertools.pairwise(prev)
        next_line = list(map(lambda x: x[1] - x[0], couples))
        triangle.append(next_line)
        prev = next_line
    return triangle


def extend_triangle(triangle: List[List[int]]) -> List[List[int]]:
    zeros = triangle[0]
    zeros.append(0)
    new_triangle = [zeros]
    for line in triangle[1:]:
        new_line = line
        new_line.append(line[-1] + new_triangle[-1][-1])
        new_triangle.append(new_line)
    return new_triangle


def parse_integers(line):
    pass


def predict_next_value(line: str) -> int:
    initial_sequence: List[int] = parse_integers(line)
    reversed_initial_triangle = list(
        reversed(assemble_triangle(initial_sequence))
    )
    final_triangle: List[List[int]] = extend_triangle(reversed_initial_triangle)
    return final_triangle[-1][-1]


def main(lines: List[str]) -> int:
    predictions = [predict_next_value(line) for line in lines]
    return sum(predictions)


def part_two_main(lines: List[str]) -> int:
    pass


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        file_lines = file.readlines()
    first_answer = main(file_lines)
    print("The first answer is", first_answer)
    second_answer = part_two_main(file_lines)
    print("The second answer is", second_answer)
