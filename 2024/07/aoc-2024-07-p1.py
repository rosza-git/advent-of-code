import sys
import itertools

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

operators = ["+", "*"]
equations = []
for line in content.splitlines():
    equations.append(line.split(" "))

total_calib_res = 0


def op_combinations(length):
    return [list(p) for p in itertools.product(operators, repeat=length)]


for equation in equations:
    result = eval(equation[0][:-1])
    nums = equation[1:]

    ops = op_combinations(len(nums) - 1)
    # print(f"{result} ?= {nums}  - {ops}")

    for op in ops:
        temp_val = 0
        temp_eq = ""
        for i in range(len(op)):
            if i == 0:
                temp_str = f"{nums[i]}{op[i]}{nums[i + 1]}"
                temp_val = eval(temp_str)
                # print(f"{temp_str} = {temp_val}")
                temp_eq = temp_str
            else:
                temp_str = f"{temp_val}{op[i]}{nums[i + 1]}"
                temp_val = eval(temp_str)
                # print(f"{temp_str} = {temp_val}")
                temp_eq += f"{op[i]}{nums[i + 1]}"

        
        if temp_val == result:
            print(f"\033[0;32m{result} == {temp_eq}\033[0m")
            total_calib_res += temp_val
            break


print(f"\nThe sum of the test values is {total_calib_res}\n")