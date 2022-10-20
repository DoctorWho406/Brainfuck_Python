import re


class BrainfuckMachine():
    class HeadOverflow(Exception):
        def __init__(self):
            super().__init__('HEAD OVERFLOW EXCEPTION. Tape limit reached')

    class BracketMismatch(Exception):
        def __init__(self):
            super().__init__('BRACKET MISMATCH EXCEPTION')

    def __init__(self, length: int = 8) -> None:
        self.tape = [0] * length
        self.code = ''
        self.head = 0

    def sum(self, value) -> None:
        self.tape[self.head] = (self.tape[self.head] + value) % 256

    def move_head(self, value) -> None:
        self.head += value
        if (self.head < 0):
            raise self.HeadOverflow
        elif (self.head >= len(self.tape)):
            raise self.HeadOverflow

    def build_brackets(self) -> dict:
        start_brackets = []
        brackets_position = {}

        brackets = re.finditer('[\\[\\]]', self.code)

        for bracket in brackets:
            if bracket.group() == '[':
                start_brackets.append(bracket.span()[0])
            elif bracket.group() == ']':
                try:
                    start_index = start_brackets.pop()
                except IndexError:
                    raise self.BracketMismatch
                brackets_position[start_index] = bracket.span()[0]
                brackets_position[bracket.span()[0]] = start_index

        if len(start_brackets) > 0:
            raise self.BracketMismatch

        return brackets_position

    def run(self) -> None:
        current_index = 0
        # I preferred to throw the BracketMismatch exception
        # before running the code for greater consistency
        #
        # The same result could be achieved with a Stack
        brackets = self.build_brackets()
        while current_index < len(self.code):
            match self.code[current_index]:
                case '+':
                    self.sum(1)
                    current_index += 1
                case '-':
                    self.sum(-1)
                    current_index += 1
                case '>':
                    self.move_head(+1)
                    current_index += 1
                case '<':
                    self.move_head(-1)
                    current_index += 1
                case '.':
                    print(chr(self.tape[self.head]))
                    current_index += 1
                    pass
                case '[':
                    if self.tape[self.head] <= 0:
                        current_index = brackets[current_index] + 1
                    else:
                        current_index += 1
                case ']':
                    if self.tape[self.head] > 0:
                        current_index = brackets[current_index]
                    else:
                        current_index += 1
