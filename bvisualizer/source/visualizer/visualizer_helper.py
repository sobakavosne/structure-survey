import re as RE
import os as OS
import sys as SYS
import json as JSON
import dotenv as DOTENV


SYS.path.append('./bvisualizer')
import utility.general_helper as H

DOTENV.load_dotenv('.env')

PATTERN = RE.compile("\s+(\S+)\s+", RE.IGNORECASE)
DELIMITER = OS.getenv('DELIMITER')
N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')


def read_directoryIO(dir):
    return H.head([x[2] for x in OS.walk(dir)])


def construct_wrapped_data_list(l):
    """
    return [[FILE_NAME, WRAPPED_DATA]]
    """
    return map(lambda file_name: [
        JSON.loads(file_name),
        open(OS.path.join(N_LIST_LOG_DIR, file_name))
    ], l)


def unwrap_data(l):
    """
    return [[FILE_NAME, UNWRAPPED_DATA]]
    """
    return map(lambda bench_case: [
        H.head(bench_case),
        H.filter_empty_list(bench_case[1].readlines()[0].split(DELIMITER))
    ], l)


def extract_test_results(l):
    return map(lambda bench_case: [
        H.head(bench_case),
        H.filter_empty_list([PATTERN.findall(line)[:-2]
                            for line in bench_case[1]][1:-1])
    ], l)


def filter_test_results(l):
    return map(lambda bench_case: [
        H.head(bench_case),
        list(map(lambda lib_case: [
            H.head(lib_case),
            int(H.last(lib_case).replace(',', ''))], H.last(bench_case)))
    ], l)
