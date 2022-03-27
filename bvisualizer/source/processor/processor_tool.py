# Data processing tool

import os as OS
import dotenv as DOTENV
import processor as P


DOTENV.load_dotenv('.env')

N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')

P.run_fnc_processor(N_LIST_LOG_DIR)
