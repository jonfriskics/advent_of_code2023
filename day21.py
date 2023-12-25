import os
import re
import copy

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = """
# ...........
# .....###.#.
# .###.##..#.
# ..#.#...#..
# ....#.#....
# .##..S####.
# .##..#...#.
# .......##..
# .##.#.####.
# .##..##.##.
# ...........
# """

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

star1 = 0
star2 = 0

# star 1

matrix = []
for i in input.strip().split("\n"):
  l = list()
  for s in i:
    l.append(s)
  matrix.append(l)

starting_positions = []

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] == 'S':
            starting_positions.append((row, col))

steps = 64
max_row = len(matrix)
max_col = len(matrix[0])

final_positions = set()

while steps != 0:
    current_positions = copy.deepcopy(starting_positions)
    starting_positions = set()
    for positions in current_positions:
        row = positions[0]
        col = positions[1]

        # look up
        if row > 0:
            if matrix[row-1][col] == '#':
                pass
            else:
                starting_positions.add((row-1, col))
        # look right
        if col < max_col:
            if matrix[row][col+1] == '#':
                pass
            else:
                starting_positions.add((row, col+1))
        # look down
        if row < max_row:
            if matrix[row+1][col] == '#':
                pass
            else:
                starting_positions.add((row+1, col))
        # look left
        if col > 0:
            if matrix[row][col-1] == '#':
                pass
            else:
                starting_positions.add((row, col-1))
    steps -= 1
    if steps == 0:
        star1 = len(starting_positions)

s = set()

# star 2

print(f"star 1: {star1}")
print(f"star 2: {star2}")