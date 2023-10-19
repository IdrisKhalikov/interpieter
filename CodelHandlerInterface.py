from stack import Stack
from Pointer import Pointer
from DebugOutput import DebugOutput

COLOR_MAP = {
    0xFFC0C0: (0, 0), 0xFFFFC0: (0, 1), 0xC0FFC0: (0, 2), 0xC0FFFF: (0, 3), 0xC0C0FF: (0, 4), 0xFFC0FF: (0, 5),
    0xFF0000: (1, 0), 0xFFFF00: (1, 1), 0x00FF00: (1, 2), 0x00FFFF: (1, 3), 0x0000FF: (1, 4), 0xFF00FF: (1, 5),
    0xC00000: (2, 0), 0xC0C000: (2, 1), 0x00C000: (2, 2), 0x00C0C0: (2, 3), 0x0000C0: (2, 4), 0xC000C0: (2, 5)
}

BLACK_COLOR = 0x000000
WHITE_COLOR = 0xFFFFFF


class CodelHandlerInterface:
    def __init__(self, debugger):
        self._direction = Pointer(1, 0)
        self._codel_chooser = Pointer(0, -1)
        self._retry_counter = 0
        self._func_table = {
            self._none_func: 'None',
            self._add: 'Add',
            self._divide: 'Divide',
            self._greater: 'Greater',
            self._duplicate: 'Duplicate',
            self._in_char: 'In character',
            self._push: 'Push',
            self._substract: 'Substract',
            self._mod: 'Mod',
            self._pointer: 'Pointer',
            self._roll: 'Roll',
            self._out_number: 'Out number',
            self._pop: 'Pop',
            self._multiply: 'Multiply',
            self._not: 'Not',
            self._switch: 'Switch',
            self._in_number: 'In number',
            self._out_char: 'Output character'
        }

        self._finished = False
        self._stack = Stack()
        self._debug = debugger

    def _output(self, value):
        self._debug.output((str(value)))
    
    def read_value(self):
        return self._debug.get_input()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def try_invoke_command(self, first_color, second_color, value):
        if second_color == BLACK_COLOR or second_color == None:
            self._retry_counter += 1
            if self._retry_counter % 2 == 0:
                self._rotate_pointer()
            else:
                self._switch_codel_chooser()
            if self._retry_counter == 8:
                self._finished = True
                self._debug.update(self._stack, self.get_pointer(), self.get_codel_chooser())
            return False
        self._retry_counter = 0
        if first_color == WHITE_COLOR or second_color == WHITE_COLOR:
            return True
        self._invoke_command(first_color, second_color, value)
        return True

    def _invoke_command(self, first_color, second_color, value):
        first_codel = COLOR_MAP[first_color]
        second_codel = COLOR_MAP[second_color]
        brightness_offset = (second_codel[0] - first_codel[0]) % 3
        hue_offset = (second_codel[1] - first_codel[1]) % 6
        func = list(self._func_table.keys())[
            brightness_offset * 6 + hue_offset]
        name = self._func_table[func]
        self._debug.update(self._stack, self.get_pointer(),
                           self.get_codel_chooser(), hue_offset, brightness_offset, name)
        func(value)

    def program_finished(self):
        return self._finished

    def get_pointer(self):
        return Pointer(self._direction.x, self._direction.y)

    def get_codel_chooser(self):
        return Pointer(self._codel_chooser.x, self._codel_chooser.y)

    def _rotate_pointer(self):
        self._direction.rotate()
        self._codel_chooser.rotate()
        return True

    def _switch_codel_chooser(self):
        self._codel_chooser.rotate()
        self._codel_chooser.rotate()
        return True

    def _push(self, value):
        raise NotImplementedError()

    def _pop(self, value):
        raise NotImplementedError()

    def _add(self, value):
        raise NotImplementedError()

    def _substract(self, value):
        raise NotImplementedError()

    def _multiply(self, value):
        raise NotImplementedError()

    def _divide(self, value):
        raise NotImplementedError()

    def _mod(self, value):
        raise NotImplementedError()

    def _not(self, value):
        raise NotImplementedError()

    def _greater(self, value):
        raise NotImplementedError()

    def _pointer(self, value):
        raise NotImplementedError()

    def _switch(self, value):
        raise NotImplementedError()

    def _duplicate(self, value):
        raise NotImplementedError()

    def _roll(self, value):
        raise NotImplementedError()

    def _in_number(self, value):
        raise NotImplementedError()

    def _out_number(self, value):
        raise NotImplementedError()

    def _in_char(self, value):
        raise NotImplementedError()

    def _out_char(self, value):
        raise NotImplementedError()

    def _none_func(self, value):
        raise NotImplementedError()
