import re as RE
import os as OS
import sys as SYS
import json as JSON
import dotenv as DOTENV
import util.general_helper.general_helper as H

DOTENV.load_dotenv('.env')

PATTERN = RE.compile("\s+(\S+)\s+ x ([\d.]+) [\D]*", RE.IGNORECASE)
DELIMITER = OS.getenv('DELIMITER')
N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')


def read_directory(dir):
    return H.head([x[2] for x in OS.walk(dir)])


def construct_wrapped_data_list(collection):
    """
    [[FILE_NAME, WRAPPED_DATA]]
    """
    return map(lambda file: [
        JSON.loads(file),
        open(OS.path.join(N_LIST_LOG_DIR, file))
    ], collection)


def unwrap_data(collection):
    """
    [[FILE_NAME, UNWRAPPED_DATA]]
    """
    return map(lambda case: [
        H.head(case),
        H.filter_empty_list(case[1].readlines()[0].split(DELIMITER))
    ], collection)


def extract_test_results(collection):
    return list(map(lambda case: [
        H.head(case),
        H.filter_empty_list([PATTERN.findall(line) for line in case[1]])
    ], collection))


