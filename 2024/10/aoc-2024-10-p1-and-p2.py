import sys
import numpy as np


if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)


with open(sys.argv[1], "r") as f:
    content = f.read()

map = []
score = 0

for c in content.splitlines():
    map.append(list(int(num) for num in list(c)))

map = np.array(map)

# find starting points (where height is 0)
trailheads = list(zip(*np.where(map == 0)))
# possible directions
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def discover(points):
    global ratings
    curr_height = points[-1][0]
    next_height = curr_height + 1
    curr_pos = points[-1][1]

    for dx, dy in dirs:
        temp_x, temp_y = curr_pos[1] + dx, curr_pos[0] + dy
        # print(f"checking [temp_y, temp_x] {temp_y}, {temp_x} (dy, dx {dy}, {dx})")
        # print(f"0 <= temp_x {temp_x} <= map.shape[1] {map.shape[1]} is {0 <= temp_x < map.shape[1]}")
        # print(f"0 <= temp_y {temp_y} < map.shape[0] {map.shape[0]} is {0 <= temp_y < map.shape[0]}")
        # print(f"map[temp_y][temp_x] is {map[temp_y][temp_x]}")
        if 0 <= temp_x < map.shape[1] and 0 <= temp_y < map.shape[0] and map[temp_y][temp_x] == next_height:
            if next_height == 9:
                scores.add((points[0], (next_height, (temp_y, temp_x))))
                ratings += 1

            else:
                # print(f"found {next_height} in {[temp_y, temp_x]}")
                points.append((next_height, [temp_y, temp_x]))
                discover(points)


scores = set()
ratings = 0

for trailhead in trailheads:
    curr_height = map[trailhead[0]][trailhead[1]]
    trail_points = [(curr_height, trailhead)]
    discover(trail_points)

# for score in scores:
#    print(f"{score}")

print(f"The sum of the scores of all trailheads ({len(trailheads)}) the topographic map is '{len(scores)}'")

print(f"The sum of the ratings of all trailheads ({len(trailheads)}) is '{ratings}'")
