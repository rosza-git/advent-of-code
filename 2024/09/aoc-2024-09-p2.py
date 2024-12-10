import sys

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

disk_content = list(content)
disk_len = len(content)
checksum = 0
original_disk_map = []
organized_disk_map = []
disk_pass_1 = []
file_id = 0


def get_color(id):
    code = id
    while code > 7:
        code -= 8 if code > 7 else 0

    return f"\u001b[4{code}m"

def print_disk_map(map):
    print("")
    empty_color = "\u001b[32;1m"
    reset_color = "\u001b[0m"
    for m in map:
        if m[0] < 0:
            block = "." * m[1]
            color = empty_color
        else:
            block = f"{m[0]}" * m[1]
            color = get_color(m[0])

        print(f"{color}{block}{reset_color}", end="")

    print("\n")


for i in range(disk_len):
    if i % 2 == 0:
        # file
        file_size_int = eval(disk_content[i])
        original_disk_map.append([file_id, file_size_int, False])
        for i in range(file_size_int):
            disk_pass_1.append(file_id)
        # print(f"found file with id {file_id} and size {file_size_int}, new disk_pass_1 {disk_pass_1}")
        file_id += 1
    else:
        # free space
        free_space_int = eval(disk_content[i])
        original_disk_map.append([-1, free_space_int])
        for i in range(free_space_int):
            disk_pass_1.append(-1)
        # print(f"found {free_space_int} empty space, new disk_pass_1 {disk_pass_1}")


print_disk_map(original_disk_map)

organized_disk_map = original_disk_map[:]

for fb in range(len(organized_disk_map) - 1, -1, -1):
    if organized_disk_map[fb][0] > -1 and not organized_disk_map[fb][2]:
        current_file_block = organized_disk_map[fb]
        file_len = current_file_block[1]

        for eb in range(len(organized_disk_map)):
            if eb < fb:
                moved = False
                if organized_disk_map[eb][0] == -1:
                    current_empty_block = organized_disk_map[eb]
                    empty_len = current_empty_block[1]

                    if empty_len == file_len:
                        # print(f"empty_len == file_len, can move {current_file_block}")
                        current_file_block[2] = True
                        organized_disk_map[eb] = current_file_block
                        organized_disk_map[fb] = current_empty_block
                        moved = True
                        break

                    elif empty_len > file_len:
                        # print(f"empty_len > file_len, can move {current_file_block}")
                        current_file_block[2] = True
                        organized_disk_map[eb][1] = empty_len - file_len
                        organized_disk_map[fb] = [-1, file_len]
                        organized_disk_map.insert(eb, current_file_block)
                        moved = True
                        break

                    else:
                        # print(f"empty_len < file_len, cannot move {current_file_block}")
                        moved = False

                if not moved:
                    organized_disk_map[fb][2] = True

        # print_disk_map(organized_disk_map)


def calc(map):
    checksum = 0
    mapp = []
    for i in range(len(map)):
        if organized_disk_map[i][0] == -1:
            mapp += ["." for _ in range(map[i][1])]
        else:
            mapp += [map[i][0] for _ in range(map[i][1])]

    for i in range(len(mapp)):
        res = (i * mapp[i]) if mapp[i] != "." else 0
        checksum += res
        

    return checksum


checksum = calc(organized_disk_map)
print_disk_map(organized_disk_map)

print(f"\nThe checksum is {checksum}\n")
