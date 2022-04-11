import re as RE
import os as OS
import sys as SYS
import json as JSON
import dotenv as DOTENV
import itertools as I


DOTENV.load_dotenv('.env')
SYS.path.append('./bvisualizer')
import utils.general_helper as H


PATTERN = RE.compile("\s+(\S+)\s+", RE.IGNORECASE)
DELIMITER = OS.getenv('DELIMITER')
N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')


def read_directoryIO(dir): return H.head([x[2] for x in OS.walk(dir)])


def construct_wrapped_data_list(l):
  """
  returns [[FILE_NAME, WRAPPED_DATA]]
  """
  return map(lambda file_name: [
    JSON.loads(file_name),
    open(OS.path.join(N_LIST_LOG_DIR, file_name))
  ], l)


def unwrap_data(l):
  """
  returns [[FILE_NAME, UNWRAPPED_DATA]]
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
      int(H.last(lib_case).replace(',', ''))], 
      H.last(bench_case)))
  ], l)


def group_bench_cases(rule):
  """
  -- inputed list 'l' must be sorted to make elements be grouped
  -- 'rule' is used to group and sort elements
  returns lambda-function waiting for a list
  """
  return lambda l: [
    [x for x in z] for k, z
    in I.groupby(sorted(l, key=rule), rule)
  ]


def map_frst_depth(fnc): return lambda l: map(fnc, l)


def map_scnd_depth(fnc): return lambda l: map(lambda x: map(fnc, x), l)


def map_thrd_depth(fnc): 
  return lambda l: map(
    lambda x: map(
      lambda y: map(fnc, y), 
      x), 
    l)


def map_frth_depth(fnc): 
  return lambda l: map(
    lambda x: map(
      lambda y: map(
        lambda z: map(fnc, z), 
        y), 
      x), 
    l)


def map_ffth_depth(fnc): 
  return lambda l: map(
    lambda a: map(
      lambda b: map(
        lambda c: map(
          lambda d: map(fnc, d), c), 
        b), 
      a), 
    l)


def sort_thrd_depth(rule): 
  return lambda frst: map(
    lambda scnd: map(
      lambda thrd: map(
        lambda bench_case: sorted(bench_case, key=rule), 
        thrd), 
      scnd), 
    frst
  )


def construct_lib_specific_fnc_to_struct_correspondence(lib_number):
  return lambda bench_case: [
    list(map(lambda x: x, H.last(bench_case)[lib_number]))
  ]


def destruct_list(l): 
  [value] = l
  return value


def construct_struct_to_fnc_matrix(bench_case):
  return [
    H.head(bench_case),
    list(map(lambda x: x, H.last(bench_case)))
  ]


def deep_map(depth, fnc): 
  """
  -- decsends to a depth of 'depth' value
  -- (find breaking reason)
  """
  return lambda l: [deep_map(depth - 1, fnc)(*l)] if depth > 1 else list(map(fnc, l))
