import sys
import re

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

sum = 0
numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open(sys.argv[1], "r") as f:
    content = f.read()

for line in iter(content.splitlines()):
    line_numbers = ""

    for i in range(len(line)):

        for str, num in numbers.items():
            # print("looking for '{}' and '{}' in '{}'".format(str, num, line[i:]))

            str_index = line.find(str, i)
            num_index = line.find(num, i)

            if str_index == i:
                line_numbers += numbers[str]
                # print("found '{}'".format(str))

            if num_index == i:
                line_numbers += num
                # print("found '{}'".format(num))

    if len(line_numbers) == 1:
        number = line_numbers + line_numbers
    else:
        number = re.sub(r'(^.).*(.$)', r'\1\2', line_numbers)

    # print(line_numbers)
    # print(number)

    sum += eval(number)

print("The sum of all of the calibration values is: {}".format(sum))
