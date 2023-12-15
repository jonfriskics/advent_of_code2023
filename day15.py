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
# rn-1
# """

# input = """
# HASH
# """

star1 = 0
star2 = 0

def get_current_value(instruction):
    current_value = 0
    for c in instruction:
        ascii = int.from_bytes(c.encode('utf-8'))
        current_value += ascii
        current_value *= 17
        current_value = current_value % 256
    return current_value

# star 1

for line in input.strip().split("\n"):
    instructions = line.split(",")

    for instruction in instructions:
        if re.search('=',instruction):
            lens, focal_length = instruction.split('=')
        elif re.search('-',instruction):
            lens, focal_length = instruction.split('-')

        star1 += get_current_value(instruction)

# star 2


lens_slots = {}
for n in range(0,256):
    lens_slots[n] = []

for line in input.strip().split("\n"):
    instructions = line.split(",")
    for instruction in instructions:
        if re.search('=',instruction):
            lens, focal_length = instruction.split('=')

            box = get_current_value(lens)
            if any(item.split('=')[0] == lens for item in lens_slots[box]):
                for i in range(len(lens_slots[box])):
                    if lens_slots[box][i][:-2] == lens:
                        lens_slots[box][i] = instruction
            else:
                lens_slots[box].append(instruction)

        elif re.search('-',instruction):
            lens, focal_length = instruction.split('-')

            box = get_current_value(lens)
            if any(item.split('=')[0] == lens for item in lens_slots[box]):
                items_to_remove = [item for item in lens_slots[box] if item.startswith(lens)]
                lens_slots[box].remove(items_to_remove[0])

for k, v in lens_slots.items():
    for i in range(len(v)):
        box = k + 1
        slot = i + 1
        focal_length = v[i][-1]
        star2 += box * slot * int(focal_length)

print(f"star 1: {star1}")
print(f"star 2: {star2}")