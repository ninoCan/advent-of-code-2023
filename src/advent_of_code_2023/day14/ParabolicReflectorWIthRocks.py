import dataclasses
import re
from dataclasses import dataclass
from typing import List, Optional

import numpy as np

from advent_of_code_2023.day3.board import Coords


@dataclass
class ParabolicReflectorWithRocks:
    height: int
    width: int
    static_rocks: List[Coords]
    rounded_rocks: List[Coords]
    _ALLOWED_DIRECTIONS = {"north", "south", "east", "west"}
    _board: np.chararray = Optional[np.chararray]

    @property
    def total_load(self) -> int:
        return sum([self.height - rock.y for rock in self.rounded_rocks])

    def tilt(self, direction: str) -> "ParabolicReflectorWithRocks":
        if direction not in self._ALLOWED_DIRECTIONS:
            raise ValueError(f"""The input k"{direction}" is not valid!""")

        return ParabolicReflectorWithRocks(
            width=self.width,
            height=self.height,
            static_rocks=self.static_rocks,
            rounded_rocks=self._tilt_all(direction),
        )

    def _tilt_all(self, direction) -> List[Coords]:
        new_rounded_rocks = []
        for rock in self.rounded_rocks:
            if not self._would_move_outside(rock, direction):
                updated_position = self._tilt_one(rock, direction)
                new_position = (
                    updated_position
                    if self._would_move_outside(updated_position, direction)
                    else self._tilt_one(updated_position, direction)
                )
                while not updated_position == new_position:
                    updated_position = new_position
                new_rounded_rocks.append(updated_position)
        return new_rounded_rocks

    def _tilt_one(self, stone: Coords, direction: str) -> Coords:
        operations = {
            "south": lambda rock: Coords(rock.x, rock.y + 1),
            "north": lambda rock: Coords(rock.x, rock.y - 1),
            "east": lambda rock: Coords(rock.x - 1, rock.y),
            "west": lambda rock: Coords(rock.x + 1, rock.y),
        }
        operation = operations[direction]
        candidate = operation(stone)
        if (candidate not in self.static_rocks) and (
            candidate not in self.rounded_rocks
        ):
            return candidate
        else:
            return stone

    def _would_move_outside(self, rock: Coords, direction: str) -> bool:
        match direction:
            case "north":
                return rock.y == 0
            case "south":
                return rock.y == self.height
            case "east":
                return rock.x == self.width
            case "west":
                return rock.x == 0

    @classmethod
    def from_lines(cls, input_lines):
        new_height = len(input_lines)
        new_width = len(input_lines[0])
        new_static_rocks = []
        new_rounded_rocks = []
        if new_height == 0:
            return ParabolicReflectorWithRocks(
                new_height, new_width, new_static_rocks, new_rounded_rocks
            )
        static_pattern = re.compile(r"#")
        rounded_pattern = re.compile(r"O")
        for index, line in enumerate(input_lines):
            static_rocks = [
                Coords(m.start(), index) for m in static_pattern.finditer(line)
            ]
            rounded_rocks = [
                Coords(m.start(), index) for m in rounded_pattern.finditer(line)
            ]
            new_static_rocks.extend(static_rocks)
            new_rounded_rocks.extend(rounded_rocks)
        return ParabolicReflectorWithRocks(
            new_height,
            new_width,
            new_static_rocks,
            new_rounded_rocks,
        )

    @property
    def board(self) -> None:
        shape = (self.height, self.width)
        board = np.chararray(shape, unicode=True)
        board[:] = "."
        for stone in self.static_rocks:
            board[stone.tuple] = "#"
        for rock in self.rounded_rocks:
            board[rock.tuple] = "O"
        return board
