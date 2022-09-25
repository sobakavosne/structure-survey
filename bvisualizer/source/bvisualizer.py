import sys as SYS
import numpy as NP

SYS.path.append('./bvisualizer')
SYS.path.append('./bvisualizer/source/visualizer')
SYS.path.append('./bvisualizer/source/processor')

import source.visualizer.visualizer_tmp as VISUALIZER
import source.processor.processor_tool as PROCESSOR
import source.visualizer.visualizer_configuration as CFG
import utils.general_helper as H


CFG.AXES.set_xlabel('Structure size', labelpad=5)
CFG.AXES.set_ylabel('Iteration', labelpad=5)
CFG.AXES.set_zlabel('MORI', labelpad=5)

Z = NP.array(PROCESSOR.FUNCTION_TO_STRUCTURE[0]['Mori']['C++'])

def construct_model(correlation):
  return H.compose(
    VISUALIZER.append_colorbar('MORI'),
    VISUALIZER.construct_correlation_surface(
      CFG.X, 
      CFG.Y 
    )
  )(correlation)


construct_model(Z)

CFG.PLT.show()
