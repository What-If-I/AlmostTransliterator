from enums import WordStates, DigitStates


class InvalidStateError(Exception):
    pass


digit_states = {
    DigitStates.A: {
        "0": DigitStates.B,
        "1": DigitStates.D,
    },
    DigitStates.B: {"1": DigitStates.C},
    DigitStates.C: {"1": DigitStates.A},
    DigitStates.D: {"1": DigitStates.E},
    DigitStates.E: {"1": DigitStates.Fin},
    DigitStates.G: {"0": DigitStates.H},
    DigitStates.H: {"0": DigitStates.Fin},
    DigitStates.Fin: {"0": DigitStates.G},
}

word_states = {
    WordStates.A: {
        "a": WordStates.BFin,
        "b": WordStates.BFin,
        "c": WordStates.BFin,
        "d": WordStates.DFin,
    },
    WordStates.BFin: {
        "a": WordStates.BFin,
        "b": WordStates.BFin,
        "c": WordStates.BFin,
        "d": WordStates.BFin,
    },
    WordStates.DFin: {
        "b": WordStates.DFin,
        "c": WordStates.DFin,
        "d": WordStates.DFin,
    },
}


class Automation:
    def __init__(self, states_map, start_state, final_states):
        self.start_state = start_state
        self.next_states = states_map[start_state]
        self.current_state = start_state
        self.states_table = states_map
        self.final_states = final_states

    def next_state(self, value):
        next_state = self.next_states.get(value, None)
        if next_state:
            self.current_state = next_state
            self.next_states = self.states_table[self.current_state]
        else:
            raise InvalidStateError("Следующее состояние не найдено.")

    def reset_state(self):
        self.next_states = self.states_table[self.start_state]

    @property
    def in_final_state(self):
        return self.current_state in self.final_states

    @property
    def in_start_state(self):
        return self.current_state == self.start_state


def automation_factory(*args, **kwargs):

    def automation():
        return Automation(*args, **kwargs)
    return automation

digit_automation = automation_factory(digit_states, DigitStates.A,
                                      (DigitStates.Fin,))

word_automation = automation_factory(word_states, WordStates.A,
                                     (WordStates.BFin, WordStates.DFin))
