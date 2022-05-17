import sys as SYS
import numpy as NP
import varname as VARNAME


SYS.path.append('./bvisualizer')
import utils.general_helper as H


def map_surface_collection(surface_list):
  """
  -- iterate through a collection of type 
  -- [{FIGURE_LIBRARY: [{SURFACE_LIBRARY: [[speed]]}]}]
  --                     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
  --                     ^ figure object
  -- to construct NumPy arrays
  -- return [{FIGURE_LIBRARY: [{SURFACE_LIBRARY: NP.ARRAY}]}]
  """
  return H.map_object_keys(
    lambda figure_library: H.map_object_keys(
      lambda surface_library: NP.array(surface_library), 
      figure_library
    ),
    surface_list
  )


def construct_bench_surface(figure, axes):
  pass

lst = [
  {
    'C++': [
      {'Immutable': [[3,2,3]]}
    ]
  },
  {
    'Ramda': [
      {'Immutable': [[1,2,3]]}
    ]
  }
]

print(map_surface_collection(lst))

