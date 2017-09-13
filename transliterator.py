from enums import literal, CharTypesEnum


class UnrecognizedSymbol(Exception):
    pass


class Transliterator:

    def __init__(self):
        self._type_checkers = self._get_type_checkers()

    def _get_type_checkers(self):
        return (
            (self._is_char, CharTypesEnum.letter),
            (self._is_number, CharTypesEnum.digit),
            (self._is_reversed_symbol, CharTypesEnum.reserved_symbol),
            (self._is_end_row, CharTypesEnum.end_row),
            (self._is_space, CharTypesEnum.space),
            (self._is_comment, CharTypesEnum.comment)
        )

    def _is_number(self, char):
        return char in ("0", "1")

    def _is_reversed_symbol(self, char):
        return char in ":;,.(){}[]=><-+*/&\\'"

    def _is_char(self, char):
        return char in ("a", "b", "c", "d")

    def _is_space(self, value):
        return value == ' '

    def _is_end_row(self, value):
        return value == '\n'

    def _is_comment(self, value):
        return value == '#'

    def get_symbol(self, char):
        for is_type, type_ in self._type_checkers:
            if is_type(char):
                return literal(char, type_)

        raise UnrecognizedSymbol("Не удалось распознать символ.")

    def analyze(self, text):
        for char in text:
            symbol = self.get_symbol(char)
            print(f"Символ {symbol.value} распознан как {symbol.type}")
