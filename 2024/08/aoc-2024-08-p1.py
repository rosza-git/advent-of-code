import sys
import itertools
import numpy as np

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()


antenna_map = []
unique_antennas = np.array([])
antinode_locations = 0

for c in content.splitlines():
    temp = list(c)
    unique = np.unique(temp)
    unique = np.delete(unique, np.nonzero(unique == "."))
    unique_antennas = np.append(unique_antennas, unique)
    antenna_map.append(temp)

antenna_map = np.array(antenna_map)
antinode_map = [["." for _ in range(len(antenna_map))] for _ in range(len(antenna_map[0]))]
unique_antennas = np.unique(unique_antennas)


def print_map(map):
    for m in map:
        for a in list(m):
            color = "\u001b[30;1m"
            if a != "." and a != "#":
                color = "\u001b[31;1m"
            elif a == "#":
                color = "\u001b[36;1m"
            print(f"{color}{a}\u001b[0m", end="")
        
        print()


def is_inside_map(pos):
    return (pos[0] >= 0) & (pos[0] < len(antenna_map)) & (pos[1] >= 0) & (pos[1] < len(antenna_map[0]))


def place_antinode(antennas, vector1, vector2):
    antinode1_pos = antennas[0] + vector1
    antinode2_pos = antennas[1] + vector2

    # print(f"{antinode1_pos}, {antinode2_pos}")

    if is_inside_map(antinode1_pos):
        antinode_map[antinode1_pos[0]][antinode1_pos[1]] = "#"

    if is_inside_map(antinode2_pos):
        antinode_map[antinode2_pos[0]][antinode2_pos[1]] = "#"


for ua in unique_antennas:
    # find all occurrences of an antenna ("ua") in the map
    # returns two arrays, first array is the row second is the column where an antenna found
    antenna_coords = np.nonzero(antenna_map == ua)
    # pair column and row positions of "ua"
    antenna_positions = np.column_stack((antenna_coords[0], antenna_coords[1]))
    # get combinations from arra positions to get their vectors
    antenna_combo = list(itertools.combinations(antenna_positions, 2))

    # print(f"Find {ua} in map")
    # print(antenna_positions)

    for ac in antenna_combo:
        vector1 = ac[0] - ac[1]
        vector2 = ac[1] - ac[0]
        # print(f"{ac} - v1 {vector1} - v2 {vector2}")

        place_antinode(ac, vector1, vector2)


print_map(antenna_map)
print()
print_map(antinode_map)
print(unique_antennas)

antinode_locations = sum(1 for row in antinode_map for item in row if item == "#")

print(f"\nThere are {antinode_locations} unique antinodes\n")