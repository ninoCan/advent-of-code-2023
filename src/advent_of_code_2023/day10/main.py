from pathlib import Path
from typing import List

from advent_of_code_2023.day10.board import PipeBoard, PipeCoords


def main(lines: List[str]) -> int:
    board = PipeBoard(lines)
    circuit = [
        PipeCoords(board.start_position.x, board.start_position.y, value="S")
    ]
    for current in circuit:
        for neighbor in board.get_following_neighbor_pipes(current):
            if neighbor not in circuit:
                circuit.append(neighbor)
    return int(len(circuit) / 2)


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
