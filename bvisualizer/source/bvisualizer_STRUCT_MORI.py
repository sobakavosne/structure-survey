import sys as SYS
import numpy as NP

SYS.path.append('./bvisualizer')
SYS.path.append('./bvisualizer/source/visualizer')
SYS.path.append('./bvisualizer/source/processor')

import source.visualizer.visualizer as VISUALIZER
import source.processor.processor_tool as PROCESSOR


M_CPP_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[0]['C++'][0]['Mori'])
M_LODASH_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[1]['Lodash'][0]['Mori'])
M_NATIVE_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[2]['Native'][0]['Mori'])
M_RAMDA_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[3]['Ramda'][0]['Mori'])
M_UNDERSCORE_CORRELATION = NP.array(PROCESSOR.STRUCTURE_TO_FUNCTION[4]['Underscore'][0]['Mori'])

VISUALIZER.construct_model(M_CPP_CORRELATION, 'C++')
VISUALIZER.construct_model(M_LODASH_CORRELATION, 'Lodash')
VISUALIZER.construct_model(M_NATIVE_CORRELATION, 'Native')
VISUALIZER.construct_model(M_RAMDA_CORRELATION, 'Ramda')
VISUALIZER.construct_model(M_UNDERSCORE_CORRELATION, 'Underscore')

VISUALIZER.CFG.PLT.show()
