import os as OS
import dotenv as DOTENV
import processor as P


DOTENV.load_dotenv('.env')

MORI_NUM = int(OS.getenv('MORI_NUM'))
LAZY_NUM = int(OS.getenv('LAZY_NUM'))
NATIVE_NUM = int(OS.getenv('NATIVE_NUM'))
IMMUTABLE_NUM = int(OS.getenv('IMMUTABLE_NUM'))
N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')

P.run_fnc_to_struct_processorIO(N_LIST_LOG_DIR, MORI_NUM)

P.run_fnc_to_struct_processorIO(N_LIST_LOG_DIR, LAZY_NUM)

P.run_fnc_to_struct_processorIO(N_LIST_LOG_DIR, NATIVE_NUM)

P.run_fnc_to_struct_processorIO(N_LIST_LOG_DIR, IMMUTABLE_NUM)
