import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

rules = {"r": 12, "g": 13, "b": 14}

# star 1
for line in input.strip().split("\n"):
    game_number = re.search('\d+', line).group()
    is_ok = True
    cubes = line.split(':')[1].strip()
    cubes_split = cubes.split(";")

    for sets in cubes_split:
        c = sets.split(",")
        for d in c:
            if d.find('blue') != -1:
                cube_number = re.search('\d+', d).group()
                if int(cube_number) <= rules['b']:
                    is_ok = is_ok and True
                else:
                    is_ok = is_ok and False
            elif d.find('red') != -1:
                cube_number = re.search('\d+', d).group()
                if int(cube_number) <= rules['r']:
                    is_ok = is_ok and True
                else:
                    is_ok = is_ok and False
            elif d.find('green') != -1:
                cube_number = re.search('\d+', d).group()
                if int(cube_number) <= rules['g']:
                    is_ok = is_ok and True
                else:
                    is_ok = is_ok and False
    if is_ok:
        star1 += int(game_number)

# star 2
for line in input.strip().split("\n"):
    cubes = line.split(':')[1].strip()
    cubes_split = cubes.split(";")
    max_cubes = {'r': 0, 'g': 0, 'b': 0}

    for sets in cubes_split:
        c = sets.split(",")
        for d in c:
            if d.find('blue') != -1:
                cube_number = re.search('\d+', d).group()
                if int(cube_number) >= max_cubes['b']:
                    max_cubes['b'] = int(cube_number)
            elif d.find('red') != -1:
                cube_number = re.search('\d+', d).group()
                if int(cube_number) >= max_cubes['r']:
                    max_cubes['r'] = int(cube_number)
            elif d.find('green') != -1:
                cube_number = re.search('\d+', d).group()
                if int(cube_number) >= max_cubes['g']:
                    max_cubes['g'] = int(cube_number)

    power = 1
    for k, v in max_cubes.items():
        power *= v

    star2 += power

print(f"star 1: {star1}")
print(f"star 2: {star2}")