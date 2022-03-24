import operator as O
import itertools as I
import visualizer_helper as V_HELPER
import utility.general_helper as H

# X - size, items
# Y - iteration, times
# Z - speed, op/sec


def prepareBenchmarkDataIO(log_dir):
    return H.compose(
        V_HELPER.filter_test_results,
        V_HELPER.extract_test_results,
        V_HELPER.unwrap_data,
        V_HELPER.construct_wrapped_data_list,
        V_HELPER.read_directoryIO,
    )(log_dir)


def construct_struct_to_fncs_case(l, struct_name, struct_lib):
    pass


# def construct_fnc_to_structs_case(l, fnc_name, fnc_lib):
#     return filter(lambda bench_case: H.head(bench_case)['fnc'].lower() == fnc_name.lower(), l)


def construct_fnc_to_structs_case(l, fnc_name, fnc_lib):
    """
    inputed list must be sorted to make elements be grouped
    """
    return [
        [y for x, y in z] for k, z
        in I.groupby(
            sorted(l, key=lambda struct_case: H.head(struct_case)['lib']),
            lambda struct_case: H.head(struct_case)['lib']
        )
    ]
