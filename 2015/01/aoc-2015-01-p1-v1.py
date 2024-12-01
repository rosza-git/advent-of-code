import sys

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

floor = 0

with open(sys.argv[1], "r") as f:
    content = f.read()

for step in content:
    match step:
        case "(":
            floor += 1
        case ")":
            floor -= 1

print("Santa is taken to the '{}' floor".format(floor))