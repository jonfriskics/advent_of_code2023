import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = """
# RL

# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)
# """

# input = """
# LLR

# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)
# """

star1 = 0
star2 = 0

# star 1

instructions = input.strip().split("\n\n")[0]
network = input.strip().split("\n\n")[1]

network_d = {}
for line in network.strip().split("\n"):
    r = re.match("(\w+)\s\=\s\((\w+)\,\s(\w+)\)", line)
    root = r.group(1).strip()
    l_side = r.group(2).strip()
    r_side = r.group(3).strip()
    network_d[root] = (l_side, r_side)

next_step = 'AAA'
steps = 0
inst_repeating = instructions * 100000
for inst in inst_repeating:
    if next_step == 'ZZZ':
        star1 = steps
        break
    elif inst == 'L':
        next_step = network_d[next_step][0]
    elif inst == 'R':
        next_step = network_d[next_step][1]
    steps += 1

# star 2

print(f"star 1: {star1}")
print(f"star 2: {star2}")