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


I_CPP_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[0]['C++'][3]['Immutable'])
I_LODASH_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[1]['Lodash'][3]['Immutable'])
I_NATIVE_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[2]['Native'][3]['Immutable'])
I_RAMDA_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[3]['Ramda'][3]['Immutable'])
I_UNDERSCORE_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[4]['Underscore'][3]['Immutable'])

VISUALIZER.construct_model(I_CPP_CORRELATION, 'C++')
VISUALIZER.construct_model(I_LODASH_CORRELATION, 'Lodash')
VISUALIZER.construct_model(I_NATIVE_CORRELATION, 'Native')
VISUALIZER.construct_model(I_RAMDA_CORRELATION, 'Ramda')
VISUALIZER.construct_model(I_UNDERSCORE_CORRELATION, 'Underscore')

VISUALIZER.CFG.PLT.title(f'Immutable structure of max size {STRUCT_MAX} to functions')
VISUALIZER.CFG.PLT.show()
