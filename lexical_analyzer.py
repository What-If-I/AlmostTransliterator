from automation import digit_automation, word_automation
from enums import TToken, literal, TstateEnum, CharTypesEnum
from transliterator import Transliterator


class WrongWordError(Exception):
    pass


class LexicalAnalyzer:

    def __init__(self):
        self.current_word = ""
        self.word_type = TToken.word
        self.current_automate = None
        self.current_word_type = None
        self.transliterator = Transliterator()
        self.state = TstateEnum.start
        self.words = []

    def determine_automate(self, symbol):
        if symbol.type == CharTypesEnum.digit:
            self.current_automate = digit_automation()
        elif symbol.type == CharTypesEnum.letter:
            self.current_automate = word_automation()

    def determine_word_type(self, symbol):
        if symbol.type == CharTypesEnum.digit:
            self.current_word_type = TToken.number
        elif symbol.type == CharTypesEnum.letter:
            self.current_word_type = TToken.word

    def reset_automate_and_word(self):
        self.current_word = ""
        self.current_automate = None

    def append_word(self):
        self.words.append(literal(self.current_word, self.current_word_type))
        self.reset_automate_and_word()

    def analyze(self, string: str):
        for char in string:
            symbol = self.transliterator.get_symbol(char)

            if not self.current_automate:
                self.determine_automate(symbol)
                self.determine_word_type(symbol)

            if symbol.type in (CharTypesEnum.space, CharTypesEnum.end_row):
                if self.current_automate.in_final_state:
                    self.append_word()
                else:
                    raise WrongWordError("Неправильное слово!")
            elif symbol.type == CharTypesEnum.digit:
                self.current_automate.next_state(symbol.value)
                self.current_word += char
            elif symbol.type == CharTypesEnum.letter:
                self.current_automate.next_state(symbol.value)
                self.current_word += char
            else:
                raise WrongWordError("Неправильное слово!")

        if self.current_automate.in_final_state:
            self.append_word()
        else:
            raise WrongWordError("Неправильное слово!")
