import processor_handler as P_HANDLER
import utils.general_helper as H

# prepared_list = P_HANDLER.prepareBenchDataIO(log_dir)
# final_matrix = P_HANDLER.construct_fnc_to_struct_case(MORI_NUM)(prepared_list)
# labeled_matrix = P_HANDLER.set_case_label(P_HANDLER.prepareBenchDataIO(log_dir), final_matrix)
# return H.trace(labeled_matrix)


def run_fnc_to_struct_processor_IO(log_dir, struct_lib_number):
  """
  -- construct `function to structre` relation
  -- the relation shows the effect of the function implementation
  returns list of type [{STRUCT_LIBRARY: {"{'fnc': FNC_NAME, 'lib': FNC_LIBRARY }": [[speed]]}}]
  """
  return H.compose(
    P_HANDLER.set_case_label,
    P_HANDLER.construct_fnc_to_struct_case(struct_lib_number),
    P_HANDLER.prepare_bench_data_IO
  )(log_dir)


def run_struct_to_fnc_processor_IO(log_dir, struct_lib_number, fnc_lib_number):
  """
  -- construct `structure to function` relation
  -- the relation shows the effect of the structure implemention
  returns list of type [{FNC_LIBRARY: {"{'fnc': FNC_NAME, 'lib': FNC_LIBRARY }": [[speed]]}}]
  """
  return H.compose(
    P_HANDLER.construct_struct_to_fnc_case(struct_lib_number, fnc_lib_number),
    P_HANDLER.prepare_bench_data_IO
  )(log_dir)
