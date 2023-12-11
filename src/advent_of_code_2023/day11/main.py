import itertools
from pathlib import Path
from typing import List

from advent_of_code_2023.day11.Universe import Universe


def l1_distance(pair):
    pass


def main(lines: List[str]) -> int:
    past_universe = Universe(lines)
    present_universe = past_universe.expand()
    galaxies = present_universe.galaxies
    paired_galaxies = itertools.pairwise(galaxies)
    return sum(l1_distance(galaxy_pair) for galaxy_pair in paired_galaxies)


def part_two_main(lines: List[str]) -> int:
    pass


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    first_answer = main(lines)
    print("The first answer is", first_answer)
    second_answer = part_two_main(lines)
    print("The second answer is", second_answer)
