import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = """
# rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
# """

# input = """
# HASH
# """

star1 = 0
star2 = 0

# star 1


for line in input.strip().split("\n"):
    instructions = line.split(",")
    for instruction in instructions:
        current_value = 0
        for c in instruction:
            ascii = int.from_bytes(c.encode('utf-8'), byteorder='big', signed=False)
            current_value += ascii
            current_value *= 17
            current_value = current_value % 256
        star1 += current_value

# star 2

print(f"star 1: {star1}")
print(f"star 2: {star2}")