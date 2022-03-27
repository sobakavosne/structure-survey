import sys as SYS
import processor_handler as P_HANDLER


SYS.path.append('./bvisualizer')
import utility.general_helper as H


def run_fnc_processor(log_dir):
  """
  -- construct matrix: function to structres correspondence
  """
  H.compose(
    H.trace,
    P_HANDLER.construct_fnc_to_structs_case,
    P_HANDLER.prepareBenchDataIO
  )(log_dir)


def run_struct_processor(log_dir):
  """
  -- construct matrix: structure to functions correspondence
  """
  H.compose(
    H.trace,
    P_HANDLER.construct_struct_to_fncs_case,
    P_HANDLER.prepareBenchDataIO
  )(log_dir)
