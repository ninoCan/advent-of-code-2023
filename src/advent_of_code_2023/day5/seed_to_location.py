import copy
import re
from pathlib import Path
from typing import List, Dict

import numpy as np


def multiply_map_matrices(dict_copy) -> np.array:
    pass


def calculate_minimum_location(seed_maps_dict: Dict[str, List[List[int]]]) -> int:
    dict_copy = copy.deepcopy(seed_maps_dict)
    seeds = np.array(dict_copy.pop("seeds"))
    matrix_of_change = multiply_map_matrices(dict_copy)

    return np.min(np.dot(seeds, matrix_of_change))


def parse_digits(line: str) -> List[int]:
    pattern = re.compile(r'\d+')
    return pattern.findall(line)

def parse(file_lines: List[str]) -> Dict[str, List[List[int]]]:
    seed_line, *rest = file_lines
    pass

if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    seeds_and_maps = parse(lines)
    first_answer = calculate_minimum_location(seeds_and_maps)
    print("The answer is", first_answer)
    second_answer = None
    print("The final answer is", second_answer)
