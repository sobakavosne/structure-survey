import sys as SYS
import itertools as I
import processor_rule as P_RULE
import processor_helper as P_HELPER


SYS.path.append('./bvisualizer')
import utility.general_helper as H

# X - size, items
# Y - iteration, times
# Z - speed, op/sec


def prepareBenchDataIO(log_dir):
  return H.compose(
    P_HELPER.filter_test_results,
    P_HELPER.extract_test_results,
    P_HELPER.unwrap_data,
    P_HELPER.construct_wrapped_data_list,
    P_HELPER.read_directoryIO,
  )(log_dir)


def construct_struct_to_fncs_case(l):
  pass


def construct_fnc_to_structs_case(l):
  """
  returns lambda-function waiting for a list
  """
  return H.compose(
      P_HELPER.list_it,
      P_HELPER.sort_thrd_depth(P_RULE.rule_size),
      P_HELPER.map_scnd_depth(P_HELPER.group_bench_cases(P_RULE.rule_iter)),
      P_HELPER.map_fst_depth(P_HELPER.group_bench_cases(P_RULE.rule_fnc)),
      P_HELPER.group_bench_cases(P_RULE.rule_lib)
    )(l)
