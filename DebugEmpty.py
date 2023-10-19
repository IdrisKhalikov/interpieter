import os

class DebugEmpty:

    def __init__(self):
        self._output = []

    def update(self, stack, pointer, codel_chooser, hue_offset=0, brightness_offset=0, func_name='None'):
        pass
    
    def output(self, value : str):
        print(value, end='')

    def get_input(self):
        print(f'[Input]: ', end='')
        return input()