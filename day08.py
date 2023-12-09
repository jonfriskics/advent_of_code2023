import os
import re
import math

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

# input = """
# LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)
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

start1 = 'HVA'
start2 = 'HHA'
start3 = 'BVA'
start4 = 'RSA'
start5 = 'AAA'
start6 = 'NPA'

def count_steps(start, network_d, instructions_list):
    steps = 0
    i = 0
    while 1 == 1:
        if start[-1] == 'Z':
            return steps
        elif instructions_list[i] == 'L':
            start = network_d[start][0]
        elif instructions_list[i] == 'R':
            start = network_d[start][1]
        steps += 1
        if i == len(instructions_list)-1:
            i = 0
        else:
            i += 1

instructions_list = list(instructions)

star2 = math.lcm(count_steps(start1, network_d, instructions_list), count_steps(start2, network_d, instructions_list), count_steps(start3, network_d, instructions_list), count_steps(start4, network_d, instructions_list), count_steps(start5, network_d, instructions_list), count_steps(start6, network_d, instructions_list))

print(f"star 1: {star1}")
print(f"star 2: {star2}")