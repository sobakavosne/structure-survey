import processor_handler as P_HANDLER
import utils.general_helper as H


def run_fnc_to_struct_processor_IO(log_dir, struct_lib_number):
  """
  -- construct `function to structre` relation
  -- the relation shows the effect of the function implementation
  returns list of type [{STRUCTURE_LIBRARY: [{FUNCTION_LIBRARY: [[speed]]}]}]
  """
  return H.compose(
    P_HANDLER.set_case_label,
    P_HANDLER.construct_fnc_to_struct_case(struct_lib_number, log_dir),
    P_HANDLER.prepare_bench_data_IO
  )(log_dir)


def run_struct_to_fnc_processor_IO(log_dir, struct_lib_number, fnc_lib_number):
  """
  -- construct `structure to function` relation
  -- the relation shows the effect of the structure implemention
  returns list of type [{FUNCTION_LIBRARY: [{STRUCTURE_LIBRARY: [[speed]]}]}]
  """
  return H.compose(
    P_HANDLER.construct_struct_to_fnc_case(struct_lib_number, fnc_lib_number),
    P_HANDLER.prepare_bench_data_IO
  )(log_dir)
