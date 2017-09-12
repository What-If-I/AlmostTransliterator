from transliterator import UnrecognizedSymbol, Transliterator


def main():
    while True:
        text_to_analyze = input("Введите текст для анализа\n")
        transliterator = Transliterator()
        try:
            transliterator.analyze(text_to_analyze)
        except UnrecognizedSymbol:
            print("Ошибка: неправильный символ!")


if __name__ == '__main__':
    main()
