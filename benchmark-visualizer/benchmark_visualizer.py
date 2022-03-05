import re as RE
import os as OS
import sys as SYS
import json as JSON
import dotenv as DOTENV
import matplotlib.pyplot as PLT
import benchmark_visualizer_handler as BVH
import util.general_helper.general_helper as H

DOTENV.load_dotenv('.env')

DELIMITER = OS.getenv('DELIMITER')
N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')

pattern = RE.compile("\s+(\S+)\s+ x ([\d.]+) [\D]*", RE.IGNORECASE)

H.compose(
  H.trace,
  BVH.extract_test_results,
  BVH.unwrap_data,
  BVH.construct_wrapped_data_list,
  BVH.read_directory,
)(N_LIST_LOG_DIR)

# lines = H.filterEmptyList(f.readlines()[0].split(DELIMITER))
# xs = H.filterEmptyList([pattern.findall(line) for line in lines])
# name = H.head(lines).strip()
# fastest = H.last(lines).strip()

# print("name:    ", name)
# print("fastest: ", fastest)
# print("values:  ", xs)
# print(ARGV)

# PLT.scatter([op_per_sec for [(library, op_per_sec)] in xs], y, c='blue', marker='x', s=100)
# PLT.plot(x, y, color='red', linewidth=2)

# PLT.xlabel('operations/sec')
# PLT.ylabel('structure size')
# PLT.title(H.head(ARGV))

# PLT.show()
