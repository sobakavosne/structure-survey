import itertools as I
import visualizer_helper as V_HELPER
import utility.general_helper as H

# X - size, items
# Y - iteration, times
# Z - speed, op/sec


def prepareBenchmarkDataIO(log_dir):
    return H.compose(
        V_HELPER.extract_test_results,
        V_HELPER.unwrap_data,
        V_HELPER.construct_wrapped_data_list,
        V_HELPER.read_directoryIO,
    )(log_dir)


def construct_structure_fncs_case(lst, struct_name, struct_lib):
    pass


def construct_fnc_structures_case(lst, fnc_name, fnc_lib):
    """
    `fnc_name`, `fnc_lib` are case sensitive
    """
    return map(filter(lambda bench_case: H.head(bench_case)['fnc'] == fnc_name, lst))
