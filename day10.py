import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# input = """
# .....
# .S-7.
# .|.|.
# .L-J.
# .....
# """

# input = """
# ..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# """

# input = """
# 7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ
# """

'''
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
'''

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

# star 1

matrix = []
for i in input.strip().split("\n"):
  l = list()
  for s in i:
    l.append(s)
  matrix.append(l)

s_position = ()

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'S':
            s_position = (row, col)

current_position = s_position

steps = 0
points_seen = []
seen_s = 0

while seen_s < 2:
    row = current_position[0]
    col = current_position[1]
    max_row = len(matrix[0]) - 1
    max_col = len(matrix[0]) - 1

    char_n = ''
    char_e = ''
    char_s = ''
    char_w = ''

    if row == max_row and col == max_col:
        # bottom right
        # don't check any row[+1] or col[+1]
        char_n = matrix[row-1][col]
        char_e = 'X'
        char_s = 'X'
        char_w = matrix[row][col-1]
    elif row == max_row and col > 0 and col < max_col:
        # bottom
        # don't check any row[+1]
        char_n = matrix[row-1][col]
        char_e = matrix[row][col+1]
        char_s = 'X'
        char_w = matrix[row][col-1]
    elif row == max_row and col == 0:
        # bottom left
        # don't check any row[+1] or col[-1]
        char_n = matrix[row-1][col]
        char_e = matrix[row][col+1]
        char_s = 'X'
        char_w = 'X'
    elif row == 0 and col == max_col:
        # top right
        # don't check any row[-1] or col[+1]
        char_n = 'X'
        char_e = 'X'
        char_s = matrix[row+1][col]
        char_w = matrix[row][col-1]
    elif row == 0 and col == 0:
        # top left
        # don't check any row[-1] or col[-1]
        char_n = 'X'
        char_e = matrix[row][col+1]
        char_s = matrix[row+1][col]
        char_w = 'X'
    elif row == 0 and col > 0 and col < max_col:
        # top
        # don't check any row[-1]
        char_n = 'X'
        char_e = matrix[row][col+1]
        char_s = matrix[row+1][col]
        char_w = matrix[row][col-1]
    elif row > 0 and col == 0:
        # left
        # don't check any col[-1]
        char_n = matrix[row-1][col]
        char_e = matrix[row][col+1]
        char_s = matrix[row+1][col]
        char_w = 'X'
    elif row > 0 and col > 0 and col < max_col:
        # middle
        char_n = matrix[row-1][col]
        char_e = matrix[row][col+1]
        char_s = matrix[row+1][col]
        char_w = matrix[row][col-1]
    elif row > 0 and row < max_row and col == max_col:
        # right
        # don't check any col[+1]
        char_n = matrix[row-1][col]
        char_e = 'X'
        char_s = matrix[row+1][col]
        char_w = matrix[row][col-1]

    found_n = False
    found_e = False
    found_s = False
    found_w = False

    if matrix[row][col] == 'S':
        seen_s += 1

    can_go_up = True
    can_go_right = True
    can_go_down = True
    can_go_left = True

    current_step_char = matrix[row][col]
    if current_step_char == '|':
        can_go_left = False
        can_go_right = False
    elif current_step_char == '-':
        can_go_up = False
        can_go_down = False
    elif current_step_char == 'L':
        can_go_left = False
        can_go_down = False
    elif current_step_char == 'J':
        can_go_right = False
        can_go_down = False
    elif current_step_char == '7':
        can_go_up = False
        can_go_right = False
    elif current_step_char == 'F':
        can_go_up = False
        can_go_left = False
    elif current_step_char == 'S':
        can_go_up = True
        can_go_right = True
        can_go_down = True
        can_go_left = True

    if (char_n == '|' or char_n == 'F' or char_n == '7') and ((row-1, col) not in points_seen) and can_go_up:
        points_seen.append((row, col))
        steps += 1
        row -= 1
    elif (char_e == '-' or char_e == '7' or char_e == 'J') and ((row, col+1) not in points_seen) and can_go_right:
        points_seen.append((row, col))
        steps += 1
        col += 1
    elif (char_s == '|' or char_s == 'J' or char_s == 'L') and ((row+1, col) not in points_seen) and can_go_down:
        points_seen.append((row, col))
        steps += 1
        row += 1
    elif (char_w == '-' or char_w == 'F' or char_w == 'L') and ((row, col-1) not in points_seen) and can_go_left:
        points_seen.append((row, col))
        steps += 1
        col -= 1
    elif char_n == 'S' or char_e == 'S' or char_s == 'S' or char_w == 'S':
        seen_s += 1

    current_position = (row, col)

    star1 = (steps // 2) + 1

# star 2

print(f"star 1: {star1}")
print(f"star 2: {star2}")