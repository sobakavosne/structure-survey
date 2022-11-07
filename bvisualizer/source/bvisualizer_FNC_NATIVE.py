import os as OS
import sys as SYS
import numpy as NP
import dotenv as DOTENV


DOTENV.load_dotenv('.env')
STRUCT_MAX = int(OS.getenv('STRUCT_MAX'))

SYS.path.append('./bvisualizer')
SYS.path.append('./bvisualizer/source/visualizer')
SYS.path.append('./bvisualizer/source/processor')

import source.visualizer.visualizer as VISUALIZER
import source.processor.processor_tool as PROCESSOR


M_NATIVE_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[0]['Mori']['Native'])
L_NATIVE_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[1]['Lazy']['Native'])
N_NATIVE_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[2]['Native']['Native'])
I_NATIVE_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[3]['Immutable']['Native'])

VISUALIZER.construct_model(M_NATIVE_CORRELATION, 'Mori')
VISUALIZER.construct_model(L_NATIVE_CORRELATION, 'Lazy')
VISUALIZER.construct_model(N_NATIVE_CORRELATION, 'Native')
VISUALIZER.construct_model(I_NATIVE_CORRELATION, 'Immutable')

VISUALIZER.CFG.PLT.title(f'Native function to structures of max size {STRUCT_MAX}')
VISUALIZER.CFG.PLT.show()
