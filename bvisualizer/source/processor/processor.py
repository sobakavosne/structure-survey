import sys as SYS
import processor_handler as P_HANDLER


SYS.path.append('./bvisualizer')
import utils.general_helper as H

# prepared_list = P_HANDLER.prepareBenchDataIO(log_dir)
# final_matrix = P_HANDLER.construct_fnc_to_struct_case(MORI_NUM)(prepared_list)
# labeled_matrix = P_HANDLER.set_case_label(P_HANDLER.prepareBenchDataIO(log_dir), final_matrix)
# return H.trace(labeled_matrix)


def run_fnc_to_struct_processorIO(log_dir, lib_number):
  """
  -- construct `function to structre` correspondence
  returns list of type [{"{'fnc': FNC, 'lib': LIB }": [[speed]]}]
  """
  return H.compose(
    P_HANDLER.set_case_label,
    P_HANDLER.construct_fnc_to_struct_case(lib_number),
    P_HANDLER.prepareBenchDataIO
  )(log_dir)


def run_struct_to_fnc_processorIO(log_dir, lib_number):
  """
  -- construct `structure to function` correspondence
  returns list of type [{"{'fnc': FNC, 'lib': LIB }": [[speed]]}]
  """
  return H.compose(
    H.trace,
    P_HANDLER.set_case_label,
    P_HANDLER.construct_fnc_to_struct_case(lib_number),
    P_HANDLER.prepareBenchDataIO
  )(log_dir)
