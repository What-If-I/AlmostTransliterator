import enum
from enum import Enum
from collections import namedtuple


class TstateEnum(Enum):
    start = enum.auto()
    continue_ = enum.auto()
    finish = enum.auto()


class CharTypesEnum(Enum):
    letter = enum.auto()
    digit = enum.auto()
    end_row = enum.auto()
    comment = enum.auto()
    space = enum.auto()
    reserved_symbol = enum.auto()


class TToken(Enum):
    identifier = enum.auto()
    number = enum.auto()
    unknown = enum.auto()
    empty = enum.auto()
    word = enum.auto()
    left_parenthesis = enum.auto()
    right_parenthesis = enum.auto()
    dot = enum.auto()
    comma = enum.auto()


literal = namedtuple('Literal', 'value type')


class WordStates(Enum):
    A = "A"
    BFin = "B, Fin"
    DFin = "D, Fin"


class DigitStates(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    G = "G"
    H = "H"
    Fin = "Fin, F"
