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


M_LODASH_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[0]['Mori']['Lodash'])
L_LODASH_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[1]['Lazy']['Lodash'])
N_LODASH_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[2]['Native']['Lodash'])
I_LODASH_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[3]['Immutable']['Lodash'])

VISUALIZER.construct_model(M_LODASH_CORRELATION, 'Mori')
VISUALIZER.construct_model(L_LODASH_CORRELATION, 'Lazy')
VISUALIZER.construct_model(N_LODASH_CORRELATION, 'Native')
VISUALIZER.construct_model(I_LODASH_CORRELATION, 'Immutable')

VISUALIZER.CFG.PLT.title(f'Lodash function to structures of max size {STRUCT_MAX}')
VISUALIZER.CFG.PLT.show()
