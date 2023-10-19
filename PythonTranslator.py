from CodelHandlerInterface import CodelHandlerInterface

class PythonTranslator(CodelHandlerInterface):
    def __init__(self):
        super().__init__()
        self._file = open('coverted.py', "w")
    
    def __enter__(self):
        self.write('stack = []')
        return self
    
    def __exit__(self, type, value, tracback):
        self._file.close()
    
    def write(self, value):
        self._file.write(value)
        self._file.write('\n')

    def _push(self, value):
        self.write(f'stack.append({value})')

    def _pop(self, value):
        self.write(f'stack.pop()')

    def _add(self, value):
        self.write('a = stack.pop()')
        self.write('b = stack.pop()')
        self.write('stack.append(a+b)')

    def _substract(self, value):
        self.write('a = stack.pop()')
        self.write('b = stack.pop()')
        self.write('stack.append(b-a)')

    def _multiply(self, value):
        self.write('a = stack.pop()')
        self.write('b = stack.pop()')
        self.write('stack.append(a*b)')

    def _divide(self, value):
        self.write('a = stack.pop()')
        self.write('b = stack.pop()')
        self.write('stack.append(b//a)')

    def _mod(self, value):
        self.write('a = stack.pop()')
        self.write('b = stack.pop()')
        self.write('stack.append(b%%a)')

    def _not(self, value):
        self.write('a = stack.pop()')
        self.write('stack.append(1 if a == 0 else 0)')

    def _greater(self, value):
        self.write('a = stack.pop()')
        self.write('b = stack.pop()')
        self.write('stack.append(b>a)')

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
        self.write('stack.append(stack[-1])')

    def _roll(self, value):
        self.write('turns = stack.pop()')
        self.write('depth = stack.pop()')
        self.write('rotated = stack[:count - depth]')
        self.write('stack = stack[count - depth:]')
        self.write('rotated += stack[-turns:] + stack[:-turns]')
        self.write('stack = rotated')

    def _in_number(self, value):
        self.write('stack.append(int(input()))')

    def _out_number(self, value):
        self.write('print(stack.pop())')

    def _in_char(self, value):
        self.write('stack.append(ord(input()))')

    def _out_char(self, value):
        self.write('print(chr(stack.pop()))')

    def _none_func(self, value):
        raise Exception()
        