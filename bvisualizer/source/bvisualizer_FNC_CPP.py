import sys as SYS
import numpy as NP

SYS.path.append('./bvisualizer')
SYS.path.append('./bvisualizer/source/visualizer')
SYS.path.append('./bvisualizer/source/processor')

import source.visualizer.visualizer as VISUALIZER
import source.processor.processor_tool as PROCESSOR


M_CPP_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[0]['Mori']['C++'])
L_CPP_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[1]['Lazy']['C++'])
N_CPP_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[2]['Native']['C++'])
I_CPP_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[3]['Immutable']['C++'])

VISUALIZER.construct_model(M_CPP_CORRELATION, 'Mori')
VISUALIZER.construct_model(L_CPP_CORRELATION, 'Lazy')
VISUALIZER.construct_model(N_CPP_CORRELATION, 'Native')
VISUALIZER.construct_model(I_CPP_CORRELATION, 'Immutable')

VISUALIZER.CFG.PLT.show()
