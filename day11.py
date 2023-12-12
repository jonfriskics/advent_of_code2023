import os
import re
import numpy as np

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = """
# ...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# """

star1 = 0
star2 = 0

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

# print_matrix(matrix)

def check_row_for_hash(matrix, r):
    for c in range(len(matrix)):
        if matrix[r][c] == '#':
            return True
    return False

def check_col_for_hash(matrix, c):
    for r in range(len(matrix[0])):
        if matrix[r][c] == '#':
            return True
    return False

empty_rows = []
empty_cols = []

for r in range(len(matrix)):
    if not check_row_for_hash(matrix, r):
        empty_rows.append(r)
    if not check_col_for_hash(matrix, r):
        empty_cols.append(r)

empty_rows.reverse()
empty_cols.reverse()

# print(empty_rows, empty_cols)

matrix_length = len(matrix)

for empty_row in empty_rows:
    for n in range(1):
        matrix = np.insert(matrix, empty_row, np.array(["X"] * matrix_length), 0)

matrix_length = len(matrix)

for empty_col in empty_cols:
    for n in range(1):
        matrix = np.insert(matrix, empty_col, np.array(["X"] * matrix_length), 1)

hash_count = 1
hash_dictionaries = {}

for row in range(len(matrix)):
    for col in range(len(matrix[r])):
        if matrix[row][col] == '#':
            matrix[row][col] = hash_count
            hash_dictionaries[hash_count] = (row, col)
            hash_count += 1

# print_matrix(matrix)
# print(hash_dictionaries)

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

distances = []
for key in hash_dictionaries.keys():
    y1 = hash_dictionaries[key][1]
    x1 = hash_dictionaries[key][0]
    for k, v in hash_dictionaries.items():
        y2 = v[1]
        x2 = v[0]
        # print(f'galaxy {key} and {k} distance {manhattan_distance(x1, y1, x2, y2)}')
        distances.append({'g1': key, 'g2': k, 'distance': manhattan_distance(x1, y1, x2, y2)})

unique_pairs = set()
unique_data = []

for item in distances:
    pair = tuple(sorted([item['g1'], item['g2']]))
    if pair not in unique_pairs:
        unique_pairs.add(pair)
        unique_data.append(item)

# print(unique_data)

for d in unique_data:
    star1 += d['distance']


# star 2

print(f"star 1: {star1}")
print(f"star 2: {star2}")