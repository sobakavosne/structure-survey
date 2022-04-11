import os as OS
import sys as SYS
import dotenv as DOTENV
import processor_handler as P_HANDLER


SYS.path.append('./bvisualizer')
import utils.general_helper as H


DOTENV.load_dotenv('.env')

MORI_NUM = int(OS.getenv('MORI_NUM'))
LAZY_NUM = int(OS.getenv('LAZY_NUM'))
NATIVE_NUM = int(OS.getenv('NATIVE_NUM'))
IMMUTABLE_NUM = int(OS.getenv('IMMUTABLE_NUM'))


def run_fnc_mori_processorIO(log_dir):
  """
  -- construct MORI matrix: function to structre matrix
  """
  H.compose(
    P_HANDLER.construct_fnc_to_struct_case(MORI_NUM),
    P_HANDLER.prepareBenchDataIO
  )(log_dir)


def run_fnc_lazy_processorIO(log_dir):
  """
  -- construct LAZY matrix: function to structre matrix
  """
  H.compose(
    P_HANDLER.construct_fnc_to_struct_case(LAZY_NUM),
    P_HANDLER.prepareBenchDataIO
  )(log_dir)


def run_fnc_native_processorIO(log_dir):
  """
  -- construct NATIVE matrix: function to structre matrix
  """
  H.compose(
    P_HANDLER.construct_fnc_to_struct_case(NATIVE_NUM),
    P_HANDLER.prepareBenchDataIO
  )(log_dir)


def run_fnc_immutable_processorIO(log_dir):
  """
  -- construct IMMUTABLE matrix: function to structre matrix
  """
  H.compose(
    P_HANDLER.construct_fnc_to_struct_case(MORI_NUM),
    P_HANDLER.prepareBenchDataIO
  )(log_dir)


# def run_struct_processorIO(log_dir):
#   """
#   -- construct matrix: structure to function matrix
#   """
#   H.compose(
#     P_HANDLER.construct_struct_to_fnc_case(),
#     P_HANDLER.prepareBenchDataIO
#   )(log_dir)
