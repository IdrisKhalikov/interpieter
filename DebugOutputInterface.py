import os

class DebugOutputInterface:

    def __init__(self):
        self._output = []

    def update(self, stack, pointer, codel_chooser, hue_offset=0, brightness_offset=0, func_name='None'):
        raise NotImplementedError()
    
    def output(self, value : str):
        raise NotImplementedError()

    def get_input(self):
        raise NotImplementedError()