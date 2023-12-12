import os
import re
from itertools import product

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = """
# ???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1
# """

# input = """
# ?#?#?#?#?#?#?#? 1,3,1,6
# """

star1 = 0
star2 = 0

# star 1

def generate_permutations(known_positions, length):
    elements = [['.', '#'] if i not in known_positions else [known_positions[i]] for i in range(length)]
    permutations = [''.join(p) for p in product(*elements)]
    return permutations

for line in input.strip().split("\n"):
    split_line = line.split(" ")
    springs = split_line[0]
    rules = split_line[1]

    known_positions = {}
    for i in range(len(springs)):
        if springs[i] != '?':
            known_positions[i] = springs[i]

    length = len(springs)

    permutations = generate_permutations(known_positions, length)

    rules_to_compare = []
    rules_split = rules.split(',')
    for r in rules_split:
        rules_to_compare.append(int(r.strip()))

    for permutation in permutations:
        ranges = []
        range_counter = 0
        for i in range(len(permutation)):
            if i == len(permutation) - 1:
                if permutation[i] == '.':
                    if range_counter != 0:
                        ranges.append(range_counter)
                    range_counter = 0
                elif permutation[i] == '#':
                    if range_counter > 0:
                        ranges.append(range_counter + 1)
                        range_counter = 0
                    elif range_counter == 0:
                        ranges.append(1)
            elif permutation[i] == '#':
                range_counter += 1
            elif permutation[i] == '.':
                if range_counter > 0:
                    ranges.append(range_counter)
                    range_counter = 0
                range_counter += 0
        if ranges == rules_to_compare:
            star1 += 1



# star 2

for line in input.strip().split("\n"):
    break # runs too slow
    split_line = line.split(" ")
    springs = split_line[0]
    rules = split_line[1]

    print(f'{springs}')
    new_springs = ''
    new_rules = ''
    for n in range(5):
        if n == 4:
            new_springs += springs
            new_rules += rules
        else:
            new_springs += (springs + '?')
            new_rules += (rules + ',')

    known_positions = {}
    for i in range(len(springs)):
        if new_springs[i] != '?':
            known_positions[i] = new_springs[i]

    length = len(new_springs)

    permutations = generate_permutations(known_positions, length)

    rules_to_compare = []
    rules_split = new_rules.split(',')
    for r in rules_split:
        rules_to_compare.append(int(r.strip()))

    for permutation in permutations:
        ranges = []
        range_counter = 0
        for i in range(len(permutation)):
            if i == len(permutation) - 1:
                if permutation[i] == '.':
                    if range_counter != 0:
                        ranges.append(range_counter)
                    range_counter = 0
                elif permutation[i] == '#':
                    if range_counter > 0:
                        ranges.append(range_counter + 1)
                        range_counter = 0
                    elif range_counter == 0:
                        ranges.append(1)
            elif permutation[i] == '#':
                range_counter += 1
            elif permutation[i] == '.':
                if range_counter > 0:
                    ranges.append(range_counter)
                    range_counter = 0
                range_counter += 0
        if ranges == rules_to_compare:
            star2 += 1


print(f"star 1: {star1}")
print(f"star 2: {star2}")