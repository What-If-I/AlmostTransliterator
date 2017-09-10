class Stack:

    def __init__(self):
        self.stack = []

    def __getitem__(self, item):
        return self.stack[item]

    def __iter__(self):
        return iter(self.stack)

    def pop(self):
        self.stack.pop(1)

    def put(self, item):
        self.stack.insert(1, item)


class States:
    S = 'S'
    E = 'E'
    P = 'P'


RULES = {
    States.S: (States.E + States.P, ),
    States.E: ('', '*' + States.S, '+' + States.S, '-' + States.S, States.S, ),
    States.P: ("TERM1", "TERM2")
}


class SyntaxAnalyzer:

    def __init__(self):
        self.ammo = Stack()

    def init_start_state(self):
        self.ammo.put(RULES[States.E][0])
    
    def analyze_char(self, char):
        pass

    def choose_rule(self, char):
        pass

