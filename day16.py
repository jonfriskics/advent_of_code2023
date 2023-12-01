import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# star 1
# star 2

print(f"star 1: {star1}")
print(f"star 2: {star2}")