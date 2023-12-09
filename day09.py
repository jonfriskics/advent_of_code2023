import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = """
# 0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45
# """

star1 = 0
star2 = 0

# star 1

histories = []
for line in input.strip().split("\n"):
    levels = []

    split_line = [int(x) for x in line.split(" ")]

    levels.append(split_line)

    current_level = split_line

    while not all(x == 0 for x in current_level):
        new_level = []
        for i in range(len(current_level)):
            if i == len(current_level)-1:
                pass
            else:
                new_level.append(int(current_level[i+1]) - int(current_level[i]))

        current_level = new_level

        levels.append(current_level)

    levels.reverse()
    levels[0].append(0)

    for a in range(len(levels)):
        if a == len(levels) - 1:
            break
        levels[a+1].append(levels[a][-1] + levels[a+1][-1])

    histories.append(levels[-1][-1])

star1 = sum(histories)

# star 2

histories = []
for line in input.strip().split("\n"):
    levels = []

    split_line = [int(x) for x in line.split(" ")]

    levels.append(split_line)

    current_level = split_line
    while not all(x == 0 for x in current_level):

        new_level = []
        for i in range(len(current_level)):
            if i == len(current_level)-1:
                pass
            else:
                new_level.append(int(current_level[i+1]) - int(current_level[i]))

        current_level = new_level

        levels.append(current_level)

    levels.reverse()
    levels[0].insert(0, 0)

    for a in range(len(levels)):
        if a == len(levels) - 1:
            break
        levels[a+1].insert(0,levels[a+1][0] - levels[a][0])

    histories.append(levels[-1][0])

star2 = sum(histories)

print(f"star 1: {star1}")
print(f"star 2: {star2}")