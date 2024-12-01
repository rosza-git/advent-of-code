import sys

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

floor = 0

with open(sys.argv[1], "r") as f:
    content = f.read()

for i in range(len(content)):
    chr = content[i]
    match chr:
        case "(":
            floor += 1
        case ")":
            floor -= 1

    print("i: '{}' - floor: '{}'".format(i, floor))

    if floor == -1:
        break

print("Santa first entered to the basement at character '{}' floor".format(i + 1))