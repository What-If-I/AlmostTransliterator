from io import StringIO

from automation import digit_automation, word_automation
from enums import TToken, literal, TstateEnum, CharTypesEnum
from transliterator import Transliterator


class MyStringIO(StringIO):

    def get_char(self):
        return self.read(1)

    def shift_position(self, idx: int):
        cur_position = self.tell()
        shift = cur_position + idx
        self.seek(shift, 0)

    def __iter__(self):
        return iter(lambda: self.get_char(), "")


class WrongWordError(Exception):
    pass


class LexicalAnalyzer:

    def __init__(self):
        self.current_word = ""
        self.transliterator = Transliterator()
        self.state = TstateEnum.start
        self.words = []

    def _append_word(self, word):
        self.words.append(word)

    def _parse_word(self, io_stream: MyStringIO):
        word = ''
        word_type = None
        automate = None

        for char in io_stream:
            symbol = self.transliterator.get_symbol(char)

            if symbol.type not in (CharTypesEnum.digit, CharTypesEnum.letter):
                # undo char read and return
                io_stream.shift_position(-1)
                break

            if not automate:
                if symbol.type == CharTypesEnum.digit:
                    automate = digit_automation()
                    word_type = TToken.number
                elif symbol.type == CharTypesEnum.letter:
                    automate = word_automation()
                    word_type = TToken.word

            if symbol.type == CharTypesEnum.digit:
                automate.next_state(symbol.value)
                word += char
            elif symbol.type == CharTypesEnum.letter:
                automate.next_state(symbol.value)
                word += char

        if automate.in_final_state:
            return literal(word, word_type)
        else:
            raise WrongWordError("Неправильное слово!")

    def analyze(self, string: str):
        with MyStringIO(string) as string_io:
            for char in string_io:
                symbol = self.transliterator.get_symbol(char)

                if symbol.type in (CharTypesEnum.digit, CharTypesEnum.letter):
                    string_io.shift_position(-1)
                    word = self._parse_word(string_io)
                    self._append_word(word)
                elif symbol.type == CharTypesEnum.comment:
                    # skip line
                    string_io.readline()
                elif symbol.type == CharTypesEnum.space:
                    # skip space
                    pass
                else:
                    self._append_word(symbol)
