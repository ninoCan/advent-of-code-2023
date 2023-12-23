from pathlib import Path
from typing import List

from advent_of_code_2023.day23.labirinth import Labyrinth


def main(input_lines: List[str]) -> int:
    game_map = Labyrinth.parse(lines)
    paths = game_map.extract_paths()
    return paths.max_length


def part_two_main(input_lines: List[str]) -> int:
    pass


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    first_answer = main(lines)
    print("The first answer is", first_answer)
    second_answer = part_two_main(lines)
    print("The second answer is", second_answer)
