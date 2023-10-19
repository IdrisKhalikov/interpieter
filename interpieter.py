from VirtualMachine import VirtualMachine
from Interpreter import Interpreter
from ImgToPiet import get_program
from DebugEmpty import DebugEmpty
from DebugOutput import DebugOutput
import argparse
import sys
import os

def main(*args, **kwargs):
    args = get_args()
    run_program(args['path'], args['codel_size'], args['d'])
    print('\nProgram ended')

def run_program(path, codel_size, debug=False):
    program = get_program(get_path(path), codel_size)
    debugger = DebugOutput() if debug else DebugEmpty()
    Interpreter().run(program, VirtualMachine, debugger)

def get_path(filename):
    if os.path.isfile(filename):
        return filename
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            path = root + os.sep + file
            if path.endswith(filename):
                return path
    sys.exit(f'File {filename} was not found!')

def get_args():
    parser = argparse.ArgumentParser(
    description='Runs Piet programs')
    parser.add_argument('path', type = str)
    parser.add_argument('codel_size', type = int)
    debugger_args = parser.add_mutually_exclusive_group()
    debugger_args.add_argument('-d', action='store_true')
    args = vars(parser.parse_args())
    return args

if __name__ == '__main__':
    main()