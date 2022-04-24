import os as OS
import dotenv as DOTENV
import processor as P
import utils.general_helper as H


DOTENV.load_dotenv('.env')

N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')

# Make sure the order of an occurrence of the libraries
# in `makeNumListSuiteMatrixList` function is the same
# as in LIBRARIES list. The source is the following:
# ~/source/struct-master/bench-suite/suite.generator.handler.js.
# The order is determined by the order of calling of the `add` 
# function, because of the synchronicity.

LIBRARIES = [('MORI', 0), ('LAZY', 1), ('NATIVE', 2), ('IMMUTABLE', 3)]

# Find a dependence on function implementation for each structure.

FNC_TO_STRUCT = [
  {lib_name: P.run_fnc_to_struct_processor_IO(N_LIST_LOG_DIR, lib_number)}
  for lib_name, lib_number in LIBRARIES
]
