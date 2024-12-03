import sys
import re

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

muls = 0

regex = r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))"

result = re.findall(regex, content)

do = True
for r in result:
    if "don't()" in r or "do()" in r:
        do = "do()" in r
    else:
        muls += (eval(r[0]) * eval(r[1])) if do else 0

print("Result of enabled multiplications is '{}'".format(muls))
