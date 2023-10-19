from CodelHandlerInterface import CodelHandlerInterface
from stack import Stack

class VirtualMachine(CodelHandlerInterface):
    def __init__(self, debug):
        super().__init__(debug)

    def _push(self, value):
        self._stack.append(value)
        return True

    def _pop(self, value):
        if self._stack.count() <= 0:
            return False
        self._stack.pop()

    def _add(self, value):
        if self._stack.count() < 2:
            return False
        result = self._stack.pop() + self._stack.pop()
        self._stack.append(result)

    def _substract(self, value):
        if self._stack.count() < 2:
            return False
        result = -self._stack.pop() + self._stack.pop()
        self._stack.append(result)

    def _multiply(self, value):
        if self._stack.count() < 2:
            return False
        result = self._stack.pop() * self._stack.pop()
        self._stack.append(result)

    def _divide(self, value):
        if self._stack.count() < 2:
            return False
        divisor = self._stack.pop()
        result = self._stack.pop() // divisor
        self._stack.append(result)

    def _mod(self, value):
        if self._stack.count() < 2:
            return False
        divisor = self._stack.pop()
        result = self._stack.pop() % divisor
        self._stack.append(result)

    def _not(self, value):
        if self._stack.count() < 1:
            return False
        result = 0 if self._stack.pop() != 0 else 1
        self._stack.append(result)

    def _greater(self, value):
        if self._stack.count() < 2:
            return False
        result = 1 if self._stack.pop() < self._stack.pop() else 0
        self._stack.append(result)

    def _pointer(self, value):
        if self._stack.count() < 1:
            return False
        angle = self._stack.pop() % 4
        for _ in range(angle):
            self._rotate_pointer()

    def _switch(self, value):
        if self._stack.count() < 1:
            return False
        switch_count = self._stack.pop() % 2
        if switch_count != 0:
            self._codel_chooser.rotate()
            self._codel_chooser.rotate()

    def _duplicate(self, value):
        if self._stack.count() < 1:
            return False
        self._stack.append(self._stack.peek())

    def _roll(self, value):
        if self._stack.count() < 2:
            return False
        turns = self._stack.pop()
        depth = self._stack.pop()
        self._stack.roll(turns, depth)

    def _in_number(self, value):
        try:
            self._stack.append(int(self.read_value()))
        except ValueError:
            self._output('Entered value was not a number')
            self._finished = True

    def _out_number(self, value):
        if self._stack.count() < 1:
            return False
        self._output(self._stack.pop())

    def _in_char(self, value):
        try:
            self._stack.append(ord(self.read_value()))
        except TypeError:
            self._output('Entered value was not a character')
            self._finished = True

    def _out_char(self, value):
        if self._stack.count() < 1:
            return False
        self._output(chr(self._stack.pop()))

    def _none_func(self, value):
        raise Exception()
        