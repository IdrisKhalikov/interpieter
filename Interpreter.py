from CodelHandlerInterface import CodelHandlerInterface
from VirtualMachine import VirtualMachine
from ProgramSource import ProgramSource
from Pointer import Pointer

class Interpreter:

    def run(self, source : ProgramSource, codel_handler_class, debugger):
        iterator = source
        previous_codel = iterator.get_color_block(Pointer(0,0))
        with codel_handler_class(debugger) as codel_handler:
            while not codel_handler.program_finished():
                block_edge = previous_codel.get_edge(
                    codel_handler.get_pointer(), 
                    codel_handler.get_codel_chooser())
                    
                next_codel = iterator.get_color_block(
                    block_edge + codel_handler.get_pointer())
                
                codel_processed = codel_handler.try_invoke_command(
                        previous_codel.get_color(),
                        next_codel.get_color(),
                        previous_codel.get_value())
                
                if codel_processed:
                    previous_codel = next_codel
