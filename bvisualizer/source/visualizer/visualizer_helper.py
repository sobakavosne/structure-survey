import re as RE
import os as OS
import sys as SYS
import json as JSON
import dotenv as DOTENV


SYS.path.append('./bvisualizer')
import utility.general_helper as H

DOTENV.load_dotenv('.env')

PATTERN = RE.compile("\s+(\S+)\s+ x ([\d.]+) [\D]*", RE.IGNORECASE)
DELIMITER = OS.getenv('DELIMITER')
N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')


def read_directoryIO(dir):
    return H.head([x[2] for x in OS.walk(dir)])


def construct_wrapped_data_list(collection):
    """
    return [[FILE_NAME, WRAPPED_DATA]]
    """
    return map(lambda file_name: [
        JSON.loads(file_name),
        open(OS.path.join(N_LIST_LOG_DIR, file_name))
    ], collection)


def unwrap_data(collection):
    """
    return [[FILE_NAME, UNWRAPPED_DATA]]
    """
    return map(lambda bench_case: [
        H.head(bench_case),
        H.filter_empty_list(bench_case[1].readlines()[0].split(DELIMITER))
    ], collection)


def extract_test_results(collection):
    return map(lambda bench_case: [
        H.head(bench_case),
        H.filter_empty_list([PATTERN.findall(line) for line in bench_case[1]])
    ], collection)


def annotate3D(ax, s, *args, **kwargs):
    '''add anotation text s to to Axes3d ax'''

    tag = Annotation3D(s, *args, **kwargs)
    ax.add_artist(tag)
