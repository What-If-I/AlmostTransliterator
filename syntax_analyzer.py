from enums import TToken, CharTypesEnum, literal

ROW_END_TOKEN = literal('\n', CharTypesEnum.end_row)


class InvalidToken(Exception):
    pass


class Stack:

    def __init__(self):
        self.stack = []

    def __getitem__(self, item):
        return self.stack[item]

    def __iter__(self):
        return iter(self.stack)

    def __bool__(self):
        return bool(self.stack)

    def pop(self):
        return self.stack.pop(0)

    def put(self, item):
        self.stack.insert(0, item)

    def load(self, iterable):
        for item in iterable:
            self.put(item)


def open_state_s(token):
    return open_state_e, open_state_p


def open_state_p(token):
    if token.type is CharTypesEnum.operator:
        return CharTypesEnum.operator, open_state_s
    elif token.type is CharTypesEnum.end_row:
        return CharTypesEnum.end_row,
    else:
        return open_state_s,


def open_state_e(token):
    if token.type is TToken.number:
        return TToken.number,
    else:
        return TToken.word,


class SyntaxAnalyzer:

    def __init__(self):
        self.ammo = Stack()
        self._init_start_state()

    def _init_start_state(self):
        initial_states = (open_state_e, open_state_p)
        self.ammo.load(reversed(initial_states))

    def _analyze_token(self, token: TToken):
        state = self.ammo.pop()

        if callable(state):  # в стеке функция которую надо раскрыть
            new_states = state(token)
            self.ammo.load(reversed(new_states))
            return self._analyze_token(token)
        else:
            return token.type is state

    def analyze_tokens(self, tokens: (list, tuple)):
        # Явно обозначаем конец строки, т.к. он отсекается Лекс. анализатором
        tokens.append(ROW_END_TOKEN)
        for token in tokens:
            if not self._analyze_token(token):
                raise InvalidToken(f"Получен токен который не ожидался: {token}")
        return True if not self.ammo else False
