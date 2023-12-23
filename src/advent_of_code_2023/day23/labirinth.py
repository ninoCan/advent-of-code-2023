from dataclasses import dataclass

from advent_of_code_2023.day23.trie_path import TriePath
from advent_of_code_2023.day3.board import Board


@dataclass
class Labyrinth:
    world_map = Board

    @staticmethod
    def parse(input_lines: list[str]) -> 'Labyrinth':
        pass

    def extract_paths(self) -> TriePath:
        pass
