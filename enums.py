import enum
from enum import Enum
from collections import namedtuple


class CharTypesEnum(Enum):
    letter = enum.auto()
    digit = enum.auto()
    end_row = enum.auto()
    comment = enum.auto()
    space = enum.auto()
    reserved_symbol = enum.auto()

literal = namedtuple('Literal', 'value type')
