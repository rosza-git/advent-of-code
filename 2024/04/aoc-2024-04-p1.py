import sys
import re
import numpy

if len(sys.argv) < 2:
    print("Error: missing input file!")
    exit(1)

with open(sys.argv[1], "r") as f:
    content = f.read()

xmas_count = 0
xmas = "XMAS"
samx = "SAMX"
word_length = len(xmas)

lines = content.splitlines()
matrix = numpy.array([[l for l in list(line)] for line in lines])


def find_in_row(row):
    joined = "".join(row)

    return len(re.findall(xmas, joined)) + len(re.findall(samx, joined))


def find_in_matrix(m):
    local_xmas = 0

    for r in range(len(m)):
        local_xmas += find_in_row(m[r])

        # for c in range(len(m[r])):
        #     print(m[r][c], end="")

        # print("")

    return local_xmas


def find_in_diagonal(m):
    local_xmas = 0
    
    z = len(matrix[0]) - word_length

    for x in range(-1 * z, z + 1):
        d = numpy.diagonal(m, x)
        local_xmas += find_in_row(d)
        # print("".join(d))

    return local_xmas


# find normal+backward XMAS
subtotal = find_in_matrix(matrix)
xmas_count += subtotal
# print("subtotal: {}".format(subtotal))

# print("")

# find normal+backward diagonal left-2-right ↘+↖
subtotal = find_in_diagonal(matrix)
xmas_count += subtotal
# print("subtotal: {}".format(subtotal))

# print("")

# find normal+backward diagonal right-2-left ↙+↗
matrix = numpy.fliplr(matrix)
# for r in range(len(matrix)):
#     for c in range(len(matrix[r])):
#         print(matrix[r][c], end="")
#     print("")

# print("")

subtotal = find_in_diagonal(matrix)
xmas_count += subtotal
# print("subtotal: {}".format(subtotal))

# print("")

# find up+down
matrix = numpy.rot90(matrix)
subtotal = find_in_matrix(matrix)
xmas_count += subtotal
# print("subtotal: {}".format(subtotal))

print("Number of 'XMAS's is '{}'".format(xmas_count))
