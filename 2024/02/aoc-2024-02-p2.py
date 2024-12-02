import sys
import math

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

safe_reports = 0

def check_levels(levels):
    for i in range(1, len(levels)):
        diff = eval(levels[i]) - eval(levels[i - 1])

        if abs(diff) > 3 or abs(diff) < 1:
            return False

        cur_dir = math.copysign(1, diff)
        if i == 1:
            prev_dir = cur_dir
        else:
            if prev_dir != cur_dir:
                return False
            
    return True


for line in (content.splitlines()):
    is_report_safe = True
    levels = line.split(" ")

    if len(levels) == 1:
        safe_reports += 1
        continue

    temp_levels = levels[:]
    for i in range(len(levels) + 1):
        if check_levels(temp_levels):
            is_report_safe = True
            break

        is_report_safe = False
        temp_levels = levels[:]
        temp_levels.pop(i - 1)

    if is_report_safe:
        safe_reports += 1


print("There are '{}' safe reports".format(safe_reports))
