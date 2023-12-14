import os
import re
import numpy as np
import copy

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
# """

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

def rotate_matrix(m):
    return np.rot90(m, k=1, axes=(1,0))

# star 1

matrix = []
for i in input.strip().split("\n"):
    l = list()
    for s in i:
        l.append(s)
    matrix.append(l)

for col in range(len(matrix[0])):
    next_highest_row = 0
    for row in range(len(matrix)):
        if row == 0:
            if matrix[row][col] == 'O' or matrix[row][col] == '#':
                next_highest_row += 1
        else:
            if matrix[row][col] == 'O' and row == next_highest_row or matrix[row][col] == '#' and row == next_highest_row:
                next_highest_row += 1
            elif matrix[row][col] == 'O':
                matrix[next_highest_row][col] = 'O'
                matrix[row][col] = '.'
                next_highest_row += 1
            elif matrix[row][col] == '#':
                next_highest_row = row + 1
            else:
                matrix[row][col] = '.'

matrix_pos = 0
for row in range(len(matrix),0,-1):
    total_o = 0
    for c in matrix[matrix_pos]:
        if c == 'O':
            total_o += 1
    star1 += total_o * row
    matrix_pos += 1

# star 2

def cycle(matrix):
    for col in range(len(matrix[0])):
        next_highest_row = 0
        for row in range(len(matrix)):
            if row == 0:
                if matrix[row][col] == 'O' or matrix[row][col] == '#':
                    next_highest_row += 1
            else:
                if matrix[row][col] == 'O' and row == next_highest_row or matrix[row][col] == '#' and row == next_highest_row:
                    next_highest_row += 1
                elif matrix[row][col] == 'O':
                    matrix[next_highest_row][col] = 'O'
                    matrix[row][col] = '.'
                    next_highest_row += 1
                elif matrix[row][col] == '#':
                    next_highest_row = row + 1
                else:
                    matrix[row][col] = '.'

    new_matrix = rotate_matrix(matrix)
    matrix = copy.deepcopy(new_matrix)


    for col in range(len(matrix[0])):
        next_highest_row = 0
        for row in range(len(matrix)):
            if row == 0:
                if matrix[row][col] == 'O' or matrix[row][col] == '#':
                    next_highest_row += 1
            else:
                if matrix[row][col] == 'O' and row == next_highest_row or matrix[row][col] == '#' and row == next_highest_row:
                    next_highest_row += 1
                elif matrix[row][col] == 'O':
                    matrix[next_highest_row][col] = 'O'
                    matrix[row][col] = '.'
                    next_highest_row += 1
                elif matrix[row][col] == '#':
                    next_highest_row = row + 1
                else:
                    matrix[row][col] = '.'

    new_matrix = rotate_matrix(matrix)
    matrix = copy.deepcopy(new_matrix)

    for col in range(len(matrix[0])):
        next_highest_row = 0
        for row in range(len(matrix)):
            if row == 0:
                if matrix[row][col] == 'O' or matrix[row][col] == '#':
                    next_highest_row += 1
            else:
                if matrix[row][col] == 'O' and row == next_highest_row or matrix[row][col] == '#' and row == next_highest_row:
                    next_highest_row += 1
                elif matrix[row][col] == 'O':
                    matrix[next_highest_row][col] = 'O'
                    matrix[row][col] = '.'
                    next_highest_row += 1
                elif matrix[row][col] == '#':
                    next_highest_row = row + 1
                else:
                    matrix[row][col] = '.'

    new_matrix = rotate_matrix(matrix)
    matrix = copy.deepcopy(new_matrix)

    for col in range(len(matrix[0])):
        next_highest_row = 0
        for row in range(len(matrix)):
            if row == 0:
                if matrix[row][col] == 'O' or matrix[row][col] == '#':
                    next_highest_row += 1
            else:
                if matrix[row][col] == 'O' and row == next_highest_row or matrix[row][col] == '#' and row == next_highest_row:
                    next_highest_row += 1
                elif matrix[row][col] == 'O':
                    matrix[next_highest_row][col] = 'O'
                    matrix[row][col] = '.'
                    next_highest_row += 1
                elif matrix[row][col] == '#':
                    next_highest_row = row + 1
                else:
                    matrix[row][col] = '.'

    new_matrix = rotate_matrix(matrix)

    return new_matrix

print(f"star 1: {star1}")

# print(' //////////////////////////////////////////////////////// star2 //////////////////////////////////////////////////////////')

matrix = []
for i in input.strip().split("\n"):
    l = list()
    for s in i:
        l.append(s)
    matrix.append(l)

for i in range(1000000000):
    new_matrix = cycle(matrix)
    matrix = copy.deepcopy(new_matrix)
    matrix_pos = 0
    sum = 0
    for row in range(len(matrix),0,-1):
        total_o = 0
        for c in matrix[matrix_pos]:
            if c == 'O':
                total_o += 1
        sum += total_o * row
        matrix_pos += 1
    if i < 200:
        print(f'i {i} sum {sum}')
        if i == 199:
            # hand calculated the cycle for now, need to write code to do it
            star2 = 89089
            print(f"star 2: {star2}")
            break
            '''
            1,000,000,000 − 150                      # 17 step cycle starts at 150
            999,999,850 − 17 × 58,823,520 = 10       # cycle runs 58,823,520 times with remainder 10
            position 10 == 89,089                    # position 10 in the cycle is 89089
            '''