import os
import re
import copy
import numpy as np

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = """
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
# """

# input = """
# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
# """

# input = """
# #.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
# """

# input = """
# .#.#..#
# ....##.
# #..#..#
# ###....
# ..#####
# .##.##.
# .#..##.
# .#..##.
# .##.##.
# ..#####
# ###....
# #..#..#
# ....##.
# .#.#..#
# ####..#
# #.#.#..
# ....##.
# """

# input = """
# .......#.####
# #..#.##.#####
# .#...#..#....
# #..#.###.....
# .##.#..##.##.
# #####.#..####
# ....######..#
# """

# input = """
# ....#..
# ..##.##
# ..##...
# #####..
# ..##...
# ##.##..
# #.#....
# ##..#..
# ####.##
# ..###..
# ###....
# """

star1 = 0
star2 = 0

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

# star 1

def rotate_matrix(m):
    return np.rot90(m)

mirror_cols = set()
mirror_rows = set()
history = {}
input_line = 1
for line in input.strip().split("\n\n"):

    matrix = []
    for i in line.strip().split("\n"):
        l = list()
        for s in i:
            l.append(s)
        matrix.append(l)

    min_width = 0
    row = 0
    for col in range(len(matrix[row])):
        if col == 0 or col == len(matrix[row]):
            continue
        if col > int((len(matrix[row]) - 1) / 2):
            min_width = min(col - 0, len(matrix[row]) - 1 - col) + 1
        else:
            min_width = min(col - 0, len(matrix[row]) + 1 - col)
        min_width = min(col - 0, len(matrix[row]) - col)
        mirror_found = True
        for offset in range(1,min_width+1):
            if matrix[row][col-offset] == matrix[row][col+offset-1]:
                mirror_found = mirror_found and True
            else:
                mirror_found = mirror_found and False
        if mirror_found:
            mirror_found_all_rows = True
            for r in range(0,len(matrix)):
                for offset in range(1,min_width+1):
                    if matrix[r][col-offset] == matrix[r][col+offset-1]:
                        mirror_found_all_rows = mirror_found_all_rows and True
                    else:
                        mirror_found_all_rows = mirror_found_all_rows and False
                        mirror_found = False
            if mirror_found_all_rows:
                mirror_cols.add(col)

    matrix = rotate_matrix(matrix)

    row = 0
    min_width = 0
    for col in range(len(matrix[row])):
        if col == 0 or col == len(matrix[row]):
            continue
        if col > int((len(matrix[row]) - 1) / 2):
            min_width = min(col - 0, len(matrix[row]) - 1 - col) + 1
        else:
            min_width = min(col - 0, len(matrix[row]) + 1 - col)
        mirror_found = True
        for offset in range(1,min_width+1):
            if matrix[row][col-offset] == matrix[row][col+offset-1]:
                mirror_found = mirror_found and True
            else:
                mirror_found = mirror_found and False
        if mirror_found:
            mirror_found_all_rows = True
            for r in range(0,len(matrix)):
                for offset in range(1,min_width+1):
                    if matrix[r][col-offset] == matrix[r][col+offset-1]:
                        mirror_found_all_rows = mirror_found_all_rows and True
                    else:
                        mirror_found_all_rows = mirror_found_all_rows and False
                        mirror_found = False
            if mirror_found_all_rows:
                mirror_rows.add(col)

    star1 += sum(mirror_cols) + 100 * sum(mirror_rows)

    col_found = -1
    row_found = -1
    if len(mirror_cols) > 0:
        col_found = list(mirror_cols).pop()
    if len(mirror_rows) > 0:
        row_found = list(mirror_rows).pop()
    history[input_line] = {'col': [col_found], 'row': [row_found]}
    input_line += 1

    mirror_cols = set()
    mirror_rows = set()

# star 2

input_line = 1
for line in input.strip().split("\n\n"):

    matrix = []
    for i in line.strip().split("\n"):
        l = list()
        for s in i:
            l.append(s)
        matrix.append(l)

    found_new_mirror = False
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            new_matrix = copy.deepcopy(matrix)
            if matrix[row][col] == '.':
                new_matrix[row][col] = '#'
            else:
                new_matrix[row][col] = '.'

            min_width = 0
            row2 = 0
            for col in range(len(new_matrix[row2])):
                if found_new_mirror == True:
                    break
                if col == 0 or col == len(new_matrix[row2]):
                    continue
                if col > int((len(new_matrix[row2]) - 1) / 2):
                    min_width = min(col - 0, len(new_matrix[row2]) - 1 - col) + 1
                else:
                    min_width = min(col - 0, len(new_matrix[row2]) + 1 - col)
                min_width = min(col - 0, len(new_matrix[row2]) - col)
                mirror_found = True
                for offset in range(1,min_width+1):
                    if new_matrix[row2][col-offset] == new_matrix[row2][col+offset-1]:
                        mirror_found = mirror_found and True
                    else:
                        mirror_found = mirror_found and False
                if mirror_found:
                    mirror_found_all_rows = True
                    for r in range(0,len(new_matrix)):
                        for offset in range(1,min_width+1):
                            if new_matrix[r][col-offset] == new_matrix[r][col+offset-1]:
                                mirror_found_all_rows = mirror_found_all_rows and True
                            else:
                                mirror_found_all_rows = mirror_found_all_rows and False
                                mirror_found = False
                    if mirror_found_all_rows:
                        if col not in history[input_line]['col']:
                            mirror_cols.add(col)
                            found_new_mirror = True

            new_matrix = rotate_matrix(new_matrix)

            row2 = 0
            min_width = 0
            for col in range(len(new_matrix[row2])):
                if found_new_mirror == True:
                    break
                if col == 0 or col == len(new_matrix[row2]):
                    continue
                if col > int((len(new_matrix[row2]) - 1) / 2):
                    min_width = min(col - 0, len(new_matrix[row2]) - 1 - col) + 1
                else:
                    min_width = min(col - 0, len(new_matrix[row2]) + 1 - col)
                mirror_found = True
                for offset in range(1,min_width+1):
                    if new_matrix[row2][col-offset] == new_matrix[row2][col+offset-1]:
                        mirror_found = mirror_found and True
                    else:
                        mirror_found = mirror_found and False
                if mirror_found:
                    mirror_found_all_rows = True
                    for r in range(0,len(new_matrix)):
                        for offset in range(1,min_width+1):
                            if new_matrix[r][col-offset] == new_matrix[r][col+offset-1]:
                                mirror_found_all_rows = mirror_found_all_rows and True
                            else:
                                mirror_found_all_rows = mirror_found_all_rows and False
                                mirror_found = False
                    if mirror_found_all_rows:
                        if col not in history[input_line]['row']:
                            mirror_rows.add(col)
                            found_new_mirror = True

            if len(mirror_cols) > 0 or len(mirror_rows) > 0:
                star2 += sum(mirror_cols) + 100 * sum(mirror_rows)
            mirror_cols = set()
            mirror_rows = set()
    input_line += 1

print(f"star 1: {star1}")
print(f"star 2: {star2}")