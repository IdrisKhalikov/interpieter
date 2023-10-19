from DebugOutputInterface import DebugOutputInterface
import os

class DebugOutput(DebugOutputInterface):

    def __init__(self):
        self._output = []

    def update(self, stack, pointer, codel_chooser, hue_offset=0, brightness_offset=0, func_name='None'):
        os.system('cls')
        window_size = os.get_terminal_size()
        width, height = window_size.lines, window_size.columns
        print(f'Next command: {func_name}')
        stack_vals = ';'.join(str(val) for val in stack.values((width-7) // 2))
        print(f'Stack: {stack_vals}')
        print(f'Pointer: {pointer}')
        print(f'Codel chooser: {codel_chooser}')
        print(f'Color change (hue, brightnesss): {hue_offset}/{brightness_offset}')
        output = ''.join(self._output)
        print(f'[Output]: {output}')
        input()
    
    def output(self, value : str):
        self._output.extend(value.split())

    def get_input(self):
        print(f'[Input]: ')
        return input()