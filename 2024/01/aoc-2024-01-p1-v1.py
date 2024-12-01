import sys
import re

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

sum = 0

with open(sys.argv[1], "r") as f:
    content = f.read()

cleaned = re.sub(r'[a-z]', '', content)

left = []
right = []
distance = 0

for line in iter(cleaned.splitlines()):
    left.append(eval(line.split("   ")[0]))
    right.append(eval(line.split("   ")[1]))

left = sorted(left)
right = sorted(right)

for i in range(len(left)):
    if left[i] > right[i]:
        distance += left[i] - right[i]
    else:
        distance += right[i] - left[i]

print("The total distance on the lists is: {}".format(distance))
