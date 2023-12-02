"""
This module contains the modelling of the bag and the functions acting on it.
"""
from dataclasses import dataclass

@dataclass
class Bag:
    red: int
    blue: int
    green: int

