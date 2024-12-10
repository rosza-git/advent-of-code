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
disk_pass_1 = []
file_id = 0

for i in range(disk_len):
    if i % 2 == 0:
        # file
        file_size_int = eval(disk_content[i])
        original_disk_map.append([file_id, file_size_int])
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


disk_pass_1_cleaned = list(filter(lambda x: x != -1, disk_pass_1))
disk_pass_2 = []

empty_count = disk_pass_1.count(-1)

for i in range(len(disk_pass_1)):
    if len(disk_pass_1_cleaned) > 0:
        if disk_pass_1[i] == -1:
            temp = disk_pass_1_cleaned.pop()
            disk_pass_2.append(temp)
            checksum += i * temp
            # print(f"{str(i).zfill(3)}. add {temp} from clean, clean length {len(disk_pass_1_cleaned)}")
        else:
            disk_pass_2.append(disk_pass_1[i])
            disk_pass_1_cleaned.pop(0)
            checksum += i * disk_pass_1[i]
            # print(f"{str(i).zfill(3)}. add {disk_pass_1[i]} from disk_pass_1, clean length {len(disk_pass_1_cleaned)}")


# print(f"Original  disk : {original_disk_map}")
# print(f"First pass : {disk_pass_1}")
# print(f"Second pass: {disk_pass_2}")

print(f"\nThe checksum is {checksum}\n")
