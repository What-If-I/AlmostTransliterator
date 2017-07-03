from automation import digit_automation, word_automation
from enums import TToken, literal, TstateEnum, CharTypesEnum
from transliterator import Transliterator


class WrongWordError(Exception):
    pass


class LexicalAnalyzer:

    def __init__(self):
        self.current_word = ""
        self.word_type = TToken.word
        self.dig_automate = digit_automation
        self.word_automate = word_automation
        self.transliterator = Transliterator()
        self.state = TstateEnum.start
        self.words = []

        self.dig_automate.reset_state()
        self.word_automate.reset_state()

    def next_symbol(self, symbol: literal):
        if symbol.type in (CharTypesEnum.space, CharTypesEnum.end_row):
            self.state = TstateEnum.finish
        if symbol.type == CharTypesEnum.digit:
            self.current_word += symbol
        pass

    def analyze(self, string: str):
        cur_automate = None
        cur_word_type = None
        for char in string:
            symbol = self.transliterator.get_symbol(char)
            if symbol.type == CharTypesEnum.digit:
                cur_automate = self.dig_automate
                cur_word_type = TToken.number
            elif symbol.type == CharTypesEnum.letter:
                cur_automate = self.word_automate
                cur_word_type = TToken.word
            if symbol.type in (CharTypesEnum.space, CharTypesEnum.end_row):
                if cur_automate.in_final_state:
                    self.words.append(literal(self.current_word, cur_word_type))
                    self.current_word = ""
                    cur_automate.reset_state()
                else:
                    raise Exception("Неправильное слово!")
            elif symbol.type == CharTypesEnum.digit:
                cur_automate.next_state(symbol.value)
                self.current_word += char
            elif symbol.type == CharTypesEnum.letter:
                cur_automate.next_state(symbol.value)
                self.current_word += char
            else:
                raise WrongWordError("Неправильное слово!")
        if cur_automate.in_final_state or cur_automate.in_start_state:
            self.words.append(literal(self.current_word, cur_word_type))
        else:
            raise WrongWordError("Неправильное слово!")
