import sys
import re
import numpy

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

xmas_count = 0
mas = "MAS"
sam = "SAM"
word_length = len(mas)

lines = content.splitlines()
matrix = numpy.array([[l for l in list(line)] for line in lines])


def find_in_row(row):
    joined = "".join(row)

    return len(re.findall(mas, joined)) + len(re.findall(sam, joined))


def find_x_mas(m):
    d = numpy.diagonal(m)
    local_xmas_1 = find_in_row(d)

    # print("".join(d))

    m = numpy.fliplr(m)
    d = numpy.diagonal(m)
    local_xmas_2 = find_in_row(d)

    # print("".join(d))

    ret = 1 if local_xmas_1 and local_xmas_2  else 0

    # print("local_xmas_1: {}  local_xmas_2: {}  ret: {}".format(local_xmas_1, local_xmas_2, ret))

    return ret


for x in range(len(matrix) - word_length + 1):
    for y in range(len(matrix) - word_length + 1):
        sub_matrix = matrix[x:x + word_length, y:y + word_length]
        # print(sub_matrix)
        xmas_count += find_x_mas(sub_matrix)

print("Number of 'X-MAS's is '{}'".format(xmas_count))
