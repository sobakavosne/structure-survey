import os as OS
import sys as SYS
import dotenv as DOTENV
import itertools as I
import processor_rule as P_RULE
import processor_helper as P_HELPER


SYS.path.append('./bvisualizer')
import utils.general_helper as H


DOTENV.load_dotenv('.env')

MORI_NUM = int(OS.getenv('MORI_NUM'))
LAZY_NUM = int(OS.getenv('LAZY_NUM'))
NATIVE_NUM = int(OS.getenv('NATIVE_NUM'))
IMMUTABLE_NUM = int(OS.getenv('IMMUTABLE_NUM'))

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


# def construct_struct_to_fnc_case(lib_number):
#   return lambda l: H.compose(
#       H.trace,
#       H.list_it,
#       P_HELPER.map_frst_depth(P_HELPER.destruct_list),
#       P_HELPER.map_frth_depth(P_HELPER.destruct_list),
#       P_HELPER.map_ffth_depth(H.last),
#       P_HELPER.map_frth_depth(P_HELPER.construct_lib_specific_fnc_to_struct_correspondence(lib_number)),
#       P_HELPER.sort_thrd_depth(P_RULE.rule_size),
#       P_HELPER.map_scnd_depth(P_HELPER.group_bench_cases(P_RULE.rule_iter)),
#       P_HELPER.map_frst_depth(P_HELPER.group_bench_cases(P_RULE.rule_fnc)),
#       P_HELPER.group_bench_cases(P_RULE.rule_lib)
#     )(l)


def construct_fnc_to_struct_case(lib_number):
  return lambda l: H.compose(
      H.trace,
      H.list_it,
      # P_HELPER.map_frst_depth(P_HELPER.destruct_list),
      # P_HELPER.map_frth_depth(P_HELPER.destruct_list),
      # P_HELPER.map_ffth_depth(H.last),
      # P_HELPER.map_frth_depth(P_HELPER.construct_lib_specific_fnc_to_struct_correspondence(lib_number)),
      P_HELPER.sort_thrd_depth(P_RULE.rule_size),
      P_HELPER.map_scnd_depth(P_HELPER.group_bench_cases(P_RULE.rule_iter)),
      P_HELPER.map_frst_depth(P_HELPER.group_bench_cases(P_RULE.rule_fnc)),
      P_HELPER.group_bench_cases(P_RULE.rule_lib)
    )(l)
