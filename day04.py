import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = """
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """

star1 = 0
star2 = 0

# star 1
for line in input.strip().split("\n"):
    r = re.match("Card\s+(\d+):\s([0-9\s]+)\s\|\s([0-9\s]+)", line)

    numbers_you_have = r.group(3).strip().split(" ")

    winning_numbers = r.group(2).strip().split(" ")

    multiplier = 0
    for w in winning_numbers:
        if w != '':
            if w in numbers_you_have:
                multiplier += 1

    if multiplier == 0:
        pts = 0
    else:
        pts = 2 ** (multiplier - 1)

    star1 += pts

# star 2

rules = []
added = []

index = 1
for line in input.strip().split("\n"):
    r = re.match("Card\s+(\d+):\s([0-9\s]+)\s\|\s([0-9\s]+)", line)

    numbers_you_have = r.group(3).strip().split(" ")

    winning_numbers = r.group(2).strip().split(" ")

    multiplier = 0
    for w in winning_numbers:
        if w != '':
            if w in numbers_you_have:
                multiplier += 1

    game_number = int(r.group(1).strip())
    rules.append({'g': game_number, 'wins': list(range(game_number + 1, game_number + multiplier + 1))})

    added.append({'g': index, 'state': 'added'})
    index += 1

while any(d['state'] == 'added' for d in added):
    for d in added:
        if d['state'] == 'added':
            game_to_check = d['g']
            for r in rules:
                if r.get('g') == game_to_check:
                    rule_to_expand = r
                    for w in rule_to_expand['wins']:
                        added.append({'g': w, 'state': 'added'})
            d['state'] = 'processed'
        d['state'] = 'processed'
star2 = len(added)

print(f"star 1: {star1}")
print(f"star 2: {star2}")