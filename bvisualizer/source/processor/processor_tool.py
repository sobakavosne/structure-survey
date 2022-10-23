import os as OS
import sys as SYS
import json as JSON
import dotenv as DOTENV


SYS.path.append('./bvisualizer')
import processor as P
import utils.general_helper as H


DOTENV.load_dotenv('.env')

BASE_PATH = './log'
N_LIST_DATA_DIR = OS.getenv('N_LIST_DATA_DIR')
CURRENT_FNC = OS.getenv('CURRENT_FNC')
STRUCT_MAX = OS.getenv('STRUCT_MAX')

LOG_DIR = OS.path.join(BASE_PATH, N_LIST_DATA_DIR, CURRENT_FNC, STRUCT_MAX)

with open('./bvisualizer/source/configuration.json') as cfg:
  cfg = cfg.read()

CONFIG = JSON.loads(cfg)

# Make sure the order of an occurrence of the structure libraries 
# in `makeNumListSuiteMatrixList` function is the same as in 
# STRUCTURE_LIBRARIES list. The source is the following:
# ~/source/struct-master/bench-suite/suite.generator.handler.js.
# The order is determined by the order of calling of the `add` 
# function

STRUCTURE_LIBRARIES = CONFIG['STRUCTURE_LIBRARIES']

# FUNCTION_LIBRARIES list has no order and will be sorted alphabetically
# (as well as inside the data processor)

FUNCTION_LIBRARIES = H.compose(
  enumerate, 
  sorted
)(CONFIG['FUNCTION_LIBRARIES'])

# Find a correlation between function implementation and each structure

FUNCTION_TO_STRUCTURE = [
  {
    struct_lib_name: P.run_fnc_to_struct_processor_IO(
      LOG_DIR, 
      struct_lib_number
    )
  } for struct_lib_number, struct_lib_name in enumerate(STRUCTURE_LIBRARIES)
]

# Find a correlation between structure library or implementation and each function

STRUCTURE_TO_FUNCTION = [
  {
    fnc_lib_name: [
      {
        struct_lib_name: P.run_struct_to_fnc_processor_IO(
          LOG_DIR,
          struct_lib_number,
          fnc_lib_number
        )
      } for struct_lib_number, struct_lib_name in enumerate(STRUCTURE_LIBRARIES)
    ]
  } for fnc_lib_number, fnc_lib_name in FUNCTION_LIBRARIES
]
