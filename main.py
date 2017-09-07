from automation import InvalidStateError
from lexical_analyzer import LexicalAnalyzer, WrongWordError
from transliterator import UnrecognizedSymbol


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


if __name__ == '__main__':
    main()
