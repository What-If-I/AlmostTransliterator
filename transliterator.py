from enums import literal, CharTypesEnum


class UnrecognizedSymbol(Exception):
    pass


class Transliterator:
    def __init__(self):
        self._result = []

    def _is_identifier(self, char):
        pass

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

    def _add_to_result(self, value):
        self._result.insert(0, value)

    def get_symbol(self, char):
        symbol = None

        if self._is_char(char):
            symbol = literal(char, CharTypesEnum.letter)
        elif self._is_number(char):
            symbol = literal(char, CharTypesEnum.digit)
        elif self._is_reversed_symbol(char):
            symbol = literal(char, CharTypesEnum.reserved_symbol)
        elif self._is_end_row(char):
            symbol = literal(char, CharTypesEnum.end_row)
        elif self._is_space(char):
            symbol = literal(char, CharTypesEnum.space)
        elif self._is_comment(char):
            symbol = literal(char, CharTypesEnum.comment)

        if not symbol:
            raise UnrecognizedSymbol("Не удалось распознать символ.")

        return symbol

    @property
    def get_result(self):
        return self._result

    def analyze(self, text):
        for char in text:
            symbol = self.get_symbol(char)
            print(f"Символ {symbol.value} распознан как {symbol.type}")
