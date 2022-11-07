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


L_CPP_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[0]['C++'][1]['Lazy'])
L_LODASH_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[1]['Lodash'][1]['Lazy'])
L_NATIVE_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[2]['Native'][1]['Lazy'])
L_RAMDA_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[3]['Ramda'][1]['Lazy'])
L_UNDERSCORE_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[4]['Underscore'][1]['Lazy'])

VISUALIZER.construct_model(L_CPP_CORRELATION, 'C++')
VISUALIZER.construct_model(L_LODASH_CORRELATION, 'Lodash')
VISUALIZER.construct_model(L_NATIVE_CORRELATION, 'Native')
VISUALIZER.construct_model(L_RAMDA_CORRELATION, 'Ramda')
VISUALIZER.construct_model(L_UNDERSCORE_CORRELATION, 'Underscore')

VISUALIZER.CFG.PLT.title(f'Lazy structure of max size {STRUCT_MAX} to functions')
VISUALIZER.CFG.PLT.show()
