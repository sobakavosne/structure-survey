import sys as SYS
import numpy as NP

SYS.path.append('./bvisualizer')
SYS.path.append('./bvisualizer/source/visualizer')
SYS.path.append('./bvisualizer/source/processor')

import source.visualizer.visualizer as VISUALIZER
import source.processor.processor_tool as PROCESSOR


M_UNDERSCORE_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[0]['Mori']['Underscore'])
L_UNDERSCORE_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[1]['Lazy']['Underscore'])
N_UNDERSCORE_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[2]['Native']['Underscore'])
I_UNDERSCORE_CORRELATION = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[3]['Immutable']['Underscore'])

VISUALIZER.construct_model(M_UNDERSCORE_CORRELATION, 'Mori')
VISUALIZER.construct_model(L_UNDERSCORE_CORRELATION, 'Lazy')
VISUALIZER.construct_model(N_UNDERSCORE_CORRELATION, 'Native')
VISUALIZER.construct_model(I_UNDERSCORE_CORRELATION, 'Immutable')

VISUALIZER.CFG.PLT.show()
