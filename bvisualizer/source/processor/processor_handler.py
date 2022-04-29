import os as OS
import sys as SYS
import dotenv as DOTENV
import itertools as I
import processor_rule as P_RULE
import processor_helper as P_HELPER
import utils.general_helper as H


DOTENV.load_dotenv('.env')

N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')


def prepare_bench_data_IO(log_dir):
  return H.compose(
    P_HELPER.filter_test_results,
    P_HELPER.extract_test_results,
    P_HELPER.unwrap_data,
    P_HELPER.construct_wrapped_data_list,
    P_HELPER.read_directoryIO,
  )(log_dir)


def construct_fnc_to_struct_case(struct_lib_number):
  return lambda prepared_list: H.compose(
    lambda final_matrix: [final_matrix, prepare_bench_data_IO(N_LIST_LOG_DIR)],
    H.list_it,
    P_HELPER.map_frst_depth(P_HELPER.remove_zero_entry_data),
    P_HELPER.map_scnd_depth(P_HELPER.remove_zero_entry_data),
    P_HELPER.map_frst_depth(P_HELPER.destruct_list),
    P_HELPER.map_frth_depth(P_HELPER.destruct_list),
    P_HELPER.map_ffth_depth(H.last),
    P_HELPER.map_frth_depth(P_HELPER.extract_struct_lib_specific_bench_FTS(struct_lib_number)),
    P_HELPER.sort_thrd_depth(P_RULE.rule_size),
    P_HELPER.map_scnd_depth(P_HELPER.group_bench_cases(P_RULE.rule_iter)),
    P_HELPER.map_frst_depth(P_HELPER.group_bench_cases(P_RULE.rule_fnc)),
    P_HELPER.group_bench_cases(P_RULE.rule_lib)
  )(prepared_list)


def construct_struct_to_fnc_case(struct_lib_number, fnc_lib_number):
  return lambda prepared_list: H.compose(
    H.list_it,
    P_HELPER.destruct_list,
    P_HELPER.map_frst_depth(P_HELPER.remove_zero_entry_data),
    P_HELPER.map_scnd_depth(P_HELPER.remove_zero_entry_data),
    P_HELPER.map_frst_depth(P_HELPER.destruct_list),
    P_HELPER.map_frth_depth(P_HELPER.extract_struct_lib_specific_bench_STF(struct_lib_number)),
    P_HELPER.sort_thrd_depth(P_RULE.rule_size),
    H.wrap_list,
    P_HELPER.map_frst_depth(P_HELPER.group_bench_cases(P_RULE.rule_iter)),
    P_HELPER.execute_lib_number_rule(fnc_lib_number),
    P_HELPER.destruct_list,
    P_HELPER.map_frst_depth(P_HELPER.group_bench_cases(P_RULE.rule_lib)),
    P_HELPER.group_bench_cases(P_RULE.rule_fnc)
  )(prepared_list)


def set_case_label(compounded_list):
  [final_matrix, prepared_list] = compounded_list
  return H.compose(
    P_HELPER.set_label(final_matrix),
    list,
    P_HELPER.extract_label,
    P_HELPER.sort_thrd_depth(P_RULE.rule_size),
    P_HELPER.map_scnd_depth(P_HELPER.group_bench_cases(P_RULE.rule_iter)),
    P_HELPER.map_frst_depth(P_HELPER.group_bench_cases(P_RULE.rule_fnc)),
    P_HELPER.group_bench_cases(P_RULE.rule_lib)
  )(prepared_list)
