import sys
import numpy

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

map = []
for c in content.splitlines():
    map.append(list(c))

OBSTACLE = "#"
EMPTY = "."
VISITED = "X"
UP = "^"
DOWN = "V"
LEFT = "<"
RIGHT = ">"
rotation = [UP, RIGHT, DOWN, LEFT]


def is_obstacle(pos):
    return map[pos[1]][pos[0]] == OBSTACLE


def is_empty(pos):
    return map[pos[1]][pos[0]] == EMPTY


def find_guard_pos():
    for y in range(len(map)):
        for x in range(len(map[y])):
            if not is_obstacle([x, y]) and not is_empty([x, y]):
                return [x, y]


def print_map():
    row = 0
    for y in range(len(map)):
        print(f"{str(row).zfill(3)} ", end="")
        for x in range(len(map[y])):
            color = "\033[0;32m"
            if map[y][x] == OBSTACLE:
                color = "\033[0;31m"
            elif map[y][x] == VISITED or map[y][x] == UP or map[y][x] == DOWN or map[y][x] == LEFT or map[y][x] == RIGHT:
                color = "\033[0;35m"
            print(color + f"{map[y][x]}\033[0m", end="")

        row += 1

        print("")


def is_gurad_facing_up(g):
    return g == UP


def is_gurad_facing_down(g):
    return g == DOWN


def is_gurad_facing_left(g):
    return g == LEFT


def is_gurad_facing_right(g):
    return g == RIGHT


def is_guard_on_the_edge(guard_pos):
    return guard_pos[0] not in range(0, len(map[0]) - 1) or guard_pos[1] not in range(0, len(map) - 1)


def turn_guard():
    global rotation
    rotation = numpy.roll(rotation, -1)
    return rotation[0]


def walk(guard_pos, guard_facing):
    guard_left = False

    while not guard_left:
        if is_gurad_facing_up(guard_facing):
            x_velocity = 0
            y_velocity = -1
        if is_gurad_facing_down(guard_facing):
            x_velocity = 0
            y_velocity = 1
        if is_gurad_facing_left(guard_facing):
            x_velocity = -1
            y_velocity = 0
        if is_gurad_facing_right(guard_facing):
            x_velocity = 1
            y_velocity = 0

        temp_pos = [guard_pos[0] + x_velocity, guard_pos[1] + y_velocity]

        if is_obstacle(temp_pos):
            guard_facing = turn_guard()
            map[guard_pos[1]][guard_pos[0]] = guard_facing
            # print(f"Guard hit an OBSTACLE at {guard_pos}, now turning {guard_facing}")

        elif is_guard_on_the_edge(temp_pos):
            map[guard_pos[1]][guard_pos[0]] = VISITED
            guard_left = True
            print_map()
            print(f"Guard left the premise at position {guard_pos}")
            
        else:
            map[temp_pos[1]][temp_pos[0]] = guard_facing
            map[guard_pos[1]][guard_pos[0]] = VISITED
            guard_pos = temp_pos


initial_guard_pos = find_guard_pos()
initial_guard_facing = map[initial_guard_pos[1]][ initial_guard_pos[0]]

walk(initial_guard_pos, initial_guard_facing)

distinct_positions = 0

for m in map:
    for c in m:
        distinct_positions += 1 if c == VISITED else 0

print(f"... after visiting '{distinct_positions}' positions")