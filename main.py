from automation import InvalidStateError
from lexical_analyzer import LexicalAnalyzer, WrongWordError
from transliterator import UnrecognizedSymbol
from syntax_analyzer import SyntaxAnalyzer, InvalidToken


def main():
    while True:
        text_to_analyze = input("Введите текст для анализа\n")
        lexical_analyzer = LexicalAnalyzer()
        try:
            lexical_analyzer.analyze(text_to_analyze)
        except (WrongWordError, UnrecognizedSymbol, InvalidStateError):
            print("Ошибка: Неправильное слово!")
        for word in lexical_analyzer.words:
            print(f"Слово {word.value} относится к типу {word.type}.")
        analyzer = SyntaxAnalyzer()
        try:
            analyzer.analyze_tokens(lexical_analyzer.words)
        except InvalidToken as err:
            print(err)


if __name__ == '__main__':
    main()
