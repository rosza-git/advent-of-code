import sys
import re

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

muls = 0

regex = r"mul\((\d{1,3}),(\d{1,3})\)"

found_muls = re.findall(regex, content)

for mul in found_muls:
    muls += (eval(mul[0]) * eval(mul[1]))

print("Result of multiplications is '{}'".format(muls))
