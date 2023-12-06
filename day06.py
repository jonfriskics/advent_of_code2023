import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# star 1

race1 = {'time': 51, 'distance': 222}
race2 = {'time': 92, 'distance': 2031}
race3 = {'time': 68, 'distance': 1126}
race4 = {'time': 90, 'distance': 1225}

distance_traveled = 0
race1_wins = []
for hold_time in range(race1['time']+1):
    available_time = race1['time'] - hold_time
    distance_traveled = 0
    for tick in range(available_time):
        distance_traveled += hold_time
    if distance_traveled > race1['distance']:
        race1_wins.append(hold_time)

distance_traveled = 0
race2_wins = []
for hold_time in range(race2['time']):
    available_time = race2['time'] - hold_time
    distance_traveled = 0
    for tick in range(available_time):
        distance_traveled += hold_time
    if distance_traveled > race2['distance']:
        race2_wins.append(hold_time)

distance_traveled = 0
race3_wins = []
for hold_time in range(race3['time']):
    available_time = race3['time'] - hold_time
    distance_traveled = 0
    for tick in range(available_time):
        distance_traveled += hold_time
    if distance_traveled > race3['distance']:
        race3_wins.append(hold_time)

distance_traveled = 0
race4_wins = []
for hold_time in range(race4['time']):
    available_time = race4['time'] - hold_time
    distance_traveled = 0
    for tick in range(available_time):
        distance_traveled += hold_time
    if distance_traveled > race4['distance']:
        race4_wins.append(hold_time)

star1 = len(race1_wins) * len(race2_wins) * len(race3_wins) * len(race4_wins)

# star 2

star2 = 0

race_part2 = {"time": 51926890, "distance": 222203111261225}

max_hold_time = race_part2['time'] // 2

for hold_time in range(max_hold_time):
    available_time = race_part2["time"] - hold_time
    distance_traveled = hold_time * available_time

    if distance_traveled > race_part2["distance"]:
        star2 = max_hold_time - hold_time+ 1
        break

star2 = star2 * 2 - 1

print(f"star 1: {star1}")
print(f"star 2: {star2}")