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
similarity = 0

for line in iter(cleaned.splitlines()):
    left.append(eval(line.split("   ")[0]))
    right.append(eval(line.split("   ")[1]))

for num in left:
    similarity += right.count(num) * num

print("The similarity score is: {}".format(similarity))
