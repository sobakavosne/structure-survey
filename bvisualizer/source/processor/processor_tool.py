import os as OS
import sys as SYS
import dotenv as DOTENV


SYS.path.append('./bvisualizer')
import processor as P
import utils.general_helper as H


DOTENV.load_dotenv('.env')

N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')

# Make sure the order of an occurrence of the structure 
# libraries in `makeNumListSuiteMatrixList` function is the same
# as in STRUCTURE_LIBRARIES list. The source is the following:
# ~/source/struct-master/bench-suite/suite.generator.handler.js.
# The order is determined by the order of calling of the `add` 
# function, because of the synchronicity.

STRUCTURE_LIBRARIES = ['MORI', 'LAZY', 'NATIVE', 'IMMUTABLE']

# FUNCTION_LIBRARIES list has no order and will be sorted alphabetically

FUNCTION_LIBRARIES = ['Ramda', 'C++']

# Find a dependence on function implementation for each structure.

FNC_TO_STRUCT = [
  {
    struct_lib: P.run_fnc_to_struct_processor_IO(
      N_LIST_LOG_DIR, 
      struct_lib
    )
  } for struct_lib in enumerate(STRUCTURE_LIBRARIES)
]

# Find a dependence on structure library or implementation for each function.

STRUCT_TO_FNC = [
  {
    fnc_lib: P.run_struct_to_fnc_processor_IO(
      N_LIST_LOG_DIR, 
      fnc_lib
    )
  } for fnc_lib in H.compose(enumerate, sorted)(FUNCTION_LIBRARIES)
]

H.trace(STRUCT_TO_FNC)
