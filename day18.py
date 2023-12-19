import os
import re
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = """
# R 6 (#70c710)
# D 5 (#0dc571)
# L 2 (#5713f0)
# D 2 (#d2c081)
# R 2 (#59c680)
# D 2 (#411b91)
# L 5 (#8ceee2)
# U 2 (#caa173)
# L 1 (#1b58a2)
# U 2 (#caa171)
# R 2 (#7807d2)
# U 3 (#a77fa3)
# L 2 (#015232)
# U 2 (#7a21e3)
# """

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

matrix = []
for i in range(700):
  l = list()
  for s in range(700):
    l.append('.')
  matrix.append(l)

star1 = 0
star2 = 0

# star 1

current_position = (250,250)
matrix[current_position[0]][current_position[1]] = '#'

polygon_points = [(250,250)]

for line in input.strip().split("\n"):
    matches = re.search('(\w)\s+(\d+)\s+\((.+)\)', line)
    direction = matches.group(1)
    meters = int(matches.group(2))
    color = matches.group(3)

    if direction == 'R':
        for s in range(meters):
            current_position = (current_position[0],current_position[1]+1)
            matrix[current_position[0]][current_position[1]] = '#'
        polygon_points.append((current_position[0],current_position[1]))
    elif direction == 'D':
        for s in range(meters):
            current_position = (current_position[0]+1,current_position[1])
            matrix[current_position[0]][current_position[1]] = '#'
        polygon_points.append((current_position[0],current_position[1]))
    elif direction == 'U':
        for s in range(meters):
            current_position = (current_position[0]-1,current_position[1])
            matrix[current_position[0]][current_position[1]] = '#'
        polygon_points.append((current_position[0],current_position[1]))
    elif direction == 'L':
        for s in range(meters):
            current_position = (current_position[0],current_position[1]-1)
            matrix[current_position[0]][current_position[1]] = '#'
        polygon_points.append((current_position[0],current_position[1]))

polygon = Polygon(polygon_points)

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        point = Point(r, c)
        if polygon.contains(point):
            matrix[r][c] = '#'

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == '#':
            star1 += 1

# star 2

_range = 500
matrix = []
for i in range(_range):
  l = list()
  for s in range(_range):
    l.append('.')
  matrix.append(l)

current_position = (int(_range/2),int(_range/2))
matrix[current_position[0]][current_position[1]] = '#'

for line in input.strip().split("\n"):
    break # uncomment to run
    matches = re.search('(\w)\s+(\d+)\s+\((.+)\)', line)
    color = matches.group(3)
    meters = int(color[1:len(color)-1], 16)
    if color[-1] == '0':
        direction = 'R'
    elif color[-1] == '1':
        direction = 'D'
    elif color[-1] == '2':
        direction = 'L'
    elif color[-1] == '3':
        direction = 'U'
    if direction == 'R':
        for s in range(meters):
            current_position = (current_position[0],current_position[1]+1)
            matrix[current_position[0]][current_position[1]] = '#'
        polygon_points.append((current_position[0],current_position[1]))
    elif direction == 'D':
        for s in range(meters):
            current_position = (current_position[0]+1,current_position[1])
            matrix[current_position[0]][current_position[1]] = '#'
        polygon_points.append((current_position[0],current_position[1]))
    elif direction == 'U':
        for s in range(meters):
            current_position = (current_position[0]-1,current_position[1])
            matrix[current_position[0]][current_position[1]] = '#'
        polygon_points.append((current_position[0],current_position[1]))
    elif direction == 'L':
        for s in range(meters):
            current_position = (current_position[0],current_position[1]-1)
            matrix[current_position[0]][current_position[1]] = '#'
        polygon_points.append((current_position[0],current_position[1]))

polygon = Polygon(polygon_points)

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        point = Point(r, c)
        if polygon.contains(point):
            matrix[r][c] = '#'

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == '#':
            star2 += 1

print(f"star 1: {star1}")
print(f"star 2: {star2}")