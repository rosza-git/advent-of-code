import sys
import re

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

sum = 0

with open(sys.argv[1], "r") as f:
    content = f.read()

cleaned = re.sub(r'[a-z]', '', content)

for line in iter(cleaned.splitlines()):
    if len(line) == 1:
        number = line + line
    else:
        number = re.sub(r'(^.).*(.$)', r'\1\2', line)

    # print(number)
    sum += eval(number)

print("The sum of all of the calibration values is: {}".format(sum))
