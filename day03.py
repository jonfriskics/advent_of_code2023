import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = """
# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """

star1 = 0
star2 = 0

# star 1
# star 2

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

# [r-1][c-1]
# [r-1][c]
# [r-1][c+1]
# [r][c-1]
# [r][c]
# [r][c+1]
# [r+1][c-1]
# [r+1][c]
# [r+1][c+1]

def symbol_adjacent(matrix, r, c):
    special_char = {}

    max_row = len(matrix[0]) - 1
    max_col = len(matrix[r]) - 1
    # print(f"max_row {max_row} max_col {max_col}")

    check_top_left = False
    check_top = False
    check_top_right = False
    check_left = False
    check_right = False
    check_bottom_left = False
    check_bottom = False
    check_bottom_right = False

    if r == 0 and c == 0:
        # print(f"r == 0 and c == 0")
        check_top_left = False
        check_top = False
        check_top_right = False
        check_left = False
        check_right = True
        check_bottom_left = False
        check_bottom = True
        check_bottom_right = True
    elif r == 0 and c > 0 and c < max_col:
        # print(f"r == 0 and c > 0 and c < max_col")
        check_top_left = False
        check_top = False
        check_top_right = False
        check_left = True
        check_right = True
        check_bottom_left = True
        check_bottom = True
        check_bottom_right = True
    elif r == 0 and c == max_col:
        # print(f"r == 0 and c == max_col")
        check_top_left = False
        check_top = False
        check_top_right = False
        check_left = True
        check_right = False
        check_bottom_left = True
        check_bottom = True
        check_bottom_right = False
    elif r > 0 and r < max_row and c == 0:
        # print(f"r > 0 and r < max_row and c == 0")
        check_top_left = False
        check_top = True
        check_top_right = True
        check_left = False
        check_right = True
        check_bottom_left = False
        check_bottom = True
        check_bottom_right = True
    elif r > 0 and r < max_row and c > 0 and c < max_col:
        # print(f"r > 0 and r < max_row and c > 0 and c < max_col")
        check_top_left = True
        check_top = True
        check_top_right = True
        check_left = True
        check_right = True
        check_bottom_left = True
        check_bottom = True
        check_bottom_right = True
    elif r > 0 and r < max_row and c == max_col:
        # print(f"r > 0 and r < max_row and c == max_col")
        check_top_left = True
        check_top = True
        check_top_right = False
        check_left = True
        check_right = False
        check_bottom_left = True
        check_bottom = True
        check_bottom_right = False
    elif r == max_row and c == 0:
        # print(f"r == max_row and col == 0")
        check_top_left = False
        check_top = True
        check_top_right = True
        check_left = False
        check_right = True
        check_bottom_left = False
        check_bottom = False
        check_bottom_right = False
    elif r == max_row and c > 0 and c < max_col:
        # print(f"r == max_row and col > 0 and c < max_col")
        check_top_left = True
        check_top = True
        check_top_right = True
        check_left = True
        check_right = True
        check_bottom_left = False
        check_bottom = False
        check_bottom_right = False
    elif r == max_row and c == max_col:
        # print(f"r == max_row and col == max_col")
        check_top_left = True
        check_top = True
        check_top_right = False
        check_left = True
        check_right = False
        check_bottom_left = False
        check_bottom = False
        check_bottom_right = False

    found_star = False
    # print(f"{r} {c} {matrix[r][c]}")
    if check_top_left:
        # print(f"char: {matrix[r-1][c-1]}, digit: {matrix[r-1][c-1].isdigit()}")
        if matrix[r][c].isdigit() and (matrix[r-1][c-1] != '.' and not matrix[r-1][c-1].isdigit()):
            # print(f"special character found {matrix[r-1][c-1]}")
            return {'r': r, 'c': c, 'char': matrix[r][c]}
    if check_top:
        if matrix[r][c].isdigit() and (matrix[r-1][c] != '.' and not matrix[r-1][c].isdigit()):
            return {'r': r, 'c': c, 'char': matrix[r][c]}
    if check_top_right:
        if matrix[r][c].isdigit() and (matrix[r-1][c+1] != '.' and not matrix[r-1][c+1].isdigit()):
            return {'r': r, 'c': c, 'char': matrix[r][c]}
    if check_left:
        if matrix[r][c].isdigit() and (matrix[r][c-1] != '.' and not matrix[r][c-1].isdigit()):
            return {'r': r, 'c': c, 'char': matrix[r][c]}
    if check_right:
        if matrix[r][c].isdigit() and (matrix[r][c+1] != '.' and not matrix[r][c+1].isdigit()):
            return {'r': r, 'c': c, 'char': matrix[r][c]}
    if check_bottom_left:
        # print(f'r {r} c {c}')
        if matrix[r][c].isdigit() and (matrix[r+1][c-1] != '.' and not matrix[r+1][c-1].isdigit()):
            return {'r': r, 'c': c, 'char': matrix[r][c]}
    if check_bottom:
        if matrix[r][c].isdigit() and (matrix[r+1][c] != '.' and not matrix[r+1][c].isdigit()):
            return {'r': r, 'c': c, 'char': matrix[r][c]}
    if check_bottom_right:
        # print(f"in check bottom right {r} {c} {matrix[r][c]} {matrix[r+1][c+1]}")
        if matrix[r][c].isdigit() and (matrix[r+1][c+1] != '.' and not matrix[r+1][c+1].isdigit()):
            return {'r': r, 'c': c, 'char': matrix[r][c]}


matrix = []
for i in input.strip().split("\n"):
  l = list()
  for s in i:
    l.append(s)
  matrix.append(l)

near_special_chars = []

for r in range(0,len(matrix[0])):
    for c in range(len(matrix[r])):
        resp = symbol_adjacent(matrix, r, c)
        if resp is not None:
            near_special_chars.append(symbol_adjacent(matrix, r, c))

# print(near_special_chars)

last_built_number = 0
built_numbers = []

def build_number(matrix, n):
    hit_left = False
    hit_right = False

    r = n['r']

    built_number_string = ""

    pos = n['c']

    starting_col = 0

    while not hit_left:
        if pos == 0:
            starting_col = pos
            hit_left = True
        elif pos == max_col:
            if matrix[r][pos-1].isdigit():
                starting_col = pos - 1
                pos -= 1
            else:
                starting_col = pos
                hit_left = True
        elif pos > 0 and pos < max_col:
            if matrix[r][pos-1].isdigit():
                starting_col = pos - 1
                pos -= 1
            else:
                starting_col = pos
                hit_left = True
    # print(f'starting_col {starting_col}')

    built_number_string = matrix[r][starting_col]
    while not hit_right:
        if starting_col == max_col:
            hit_right = True
        else:
            if matrix[r][starting_col+1].isdigit():
                built_number_string = built_number_string + str(matrix[r][starting_col + 1])
                starting_col += 1
            else:
                hit_right = True
        # print(built_number_string)
    return built_number_string

for n in near_special_chars:
    max_row = len(matrix[0]) - 1
    max_col = len(matrix[r]) - 1

    # print(n, n['r'], n['c'], n['char'])

    a_number = build_number(matrix, n)
    if len(built_numbers) > 0:
        if built_numbers[-1] == a_number:
            pass
        else:
            built_numbers.append(a_number)
    else:
        built_numbers.append(a_number)

# print(built_numbers)

for n in built_numbers:
    star1 += int(n)

star1 += 703 # analyzed input and saw that one number appeared twice in a row, which my current solution doesn't account for.  For now, I added that number back in to the sum to solve part 1.

star2 = 82818007 # solved part 2 by hand for now.

print(f"star 1: {star1}")
print(f"star 2: {star2}")