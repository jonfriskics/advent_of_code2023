import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# star 1
for line in input.strip().split("\n"):
  num_str = ''
  for c in line:
    if c.isdigit():
      num_str = num_str + c
  num_str = num_str[0] + num_str[-1]
  star1 += int(num_str)

def word_found(s):
  if s.find('one') == 0:
    return "1"
  elif s.find('two') == 0:
    return "2"
  elif s.find('three') == 0:
    return "3"
  elif s.find('four') == 0:
    return "4"
  elif s.find('five') == 0:
    return "5"
  elif s.find('six') == 0:
    return "6"
  elif s.find('seven') == 0:
    return "7"
  elif s.find('eight') == 0:
    return "8"
  elif s.find('nine') == 0:
    return "9"
  else:
    return "0"

# star 2
for line in input.strip().split("\n"):
  new_str = ''
  for pos in range(len(line)):
    if line[pos:][0].isdigit():
      new_str += str(line[pos:][0])
    else:
      f = word_found(line[pos:])
      if f == "0":
        pass
      else:
        new_str += f

  d1 = new_str[0]
  d2 = new_str[-1]
  star2 += int(d1 + d2)

print(f"star 1: {star1}")
print(f"star 2: {star2}")