import os as OS
import sys as SYS
import numpy as NP
import dotenv as DOTENV
import matplotlib as MPL
import matplotlib.pyplot as PLT

SYS.path.append('./bvisualizer')
import utils.general_helper as H


DOTENV.load_dotenv('.env')

ITER_MAX = int(OS.getenv('ITER_MAX'))
ITER_STEP = int(OS.getenv('ITER_STEP'))
STRUCT_MAX = int(OS.getenv('STRUCT_MAX'))
STRUCT_STEP = int(OS.getenv('STRUCT_STEP'))


FIGURE = PLT.figure(figsize=(12, 12))
AXES = FIGURE.add_subplot(projection='3d')


# Visualizer configuration
PLT.style.use([PLT.style.available[0]])
MPL.rcParams['font.size'] = 8
MPL.rcParams['axes.edgecolor'] = 'black'
AXES.set_xlabel('x', labelpad=5)
AXES.set_ylabel('y', labelpad=5)
AXES.set_zlabel('z', labelpad=5)


X_AXIS = NP.arange(
  ITER_STEP, 
  ITER_MAX+ITER_STEP, 
  ITER_STEP
)

Y_AXIS = NP.arange(
  STRUCT_STEP, 
  STRUCT_MAX+STRUCT_STEP, 
  STRUCT_STEP
)

X, Y = NP.meshgrid(X_AXIS, Y_AXIS)

PLT.subplots_adjust(
  right=1, 
  left=0.03, 
  bottom=0.00,
  top=1, 
  wspace=0.0, 
  hspace=0.0
)
