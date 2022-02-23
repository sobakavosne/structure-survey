import re as RE
import os as OS
import sys as SYS
import dotenv as DOTENV
import matplotlib.pyplot as PLT
import util.general_helper.general_helper as H

DOTENV.load_dotenv('.env')

ARGV = SYS.argv[1:]
DELIMITER = OS.getenv('DELIMITER')
STRUCT_SIZE = int(OS.getenv('STRUCT_SIZE'))

pattern = RE.compile("\s+(\S+)\s+ x ([\d.]+) [\D]*", RE.IGNORECASE)

f = open("./log/number-list/Struct.Size.1000000.log")
lines = H.filterEmptyList(f.readlines()[0].split(DELIMITER))
xs = H.filterEmptyList([pattern.findall(line) for line in lines])
name = H.head(lines).strip()
fastest = H.last(lines).strip()

print("name:    ", name)
print("fastest: ", fastest)
print("values:  ", xs)
print(ARGV)

PLT.scatter([op_per_sec for [(library, op_per_sec)] in xs], y, c='blue', marker='x', s=100)
PLT.plot(x, y, color='red', linewidth=2)

PLT.xlabel('operations/sec')
PLT.ylabel('structure size')
PLT.title(H.head(ARGV))

PLT.show()
