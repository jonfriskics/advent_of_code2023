import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

input = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

seeds = []
seed_to_soil = ''
soil_to_fertilizer = ''
fertilizer_to_water = ''
water_to_light = ''
light_to_temperature = ''
temperature_to_humidity = ''
humidity_to_location = ''

rules = []
for inputs in input.strip().split("\n\n"):
    if inputs[0:5] == 'seeds':
        seeds = inputs[5:].split(' ')
        seeds.pop(0)
        seeds = [int(x) for x in seeds]
    elif inputs[0:5] == 'seed-':
        seed_to_soil = inputs
        a = inputs.split('\n')
        seed_to_soil = '\n'.join(a[1:])
    elif inputs[0:5] == 'soil-':
        soil_to_fertilizer = inputs
        a = inputs.split('\n')
        soil_to_fertilizer = '\n'.join(a[1:])
    elif inputs[0:5] == 'ferti':
        fertilizer_to_water = inputs
        a = inputs.split('\n')
        fertilizer_to_water = '\n'.join(a[1:])
    elif inputs[0:5] == 'water':
        water_to_light = inputs
        a = inputs.split('\n')
        water_to_light = '\n'.join(a[1:])
    elif inputs[0:5] == 'light':
        light_to_temperature = inputs
        a = inputs.split('\n')
        light_to_temperature = '\n'.join(a[1:])
    elif inputs[0:5] == 'tempe':
        temperature_to_humidity = inputs
        a = inputs.split('\n')
        temperature_to_humidity = '\n'.join(a[1:])
    elif inputs[0:5] == 'humid':
        humidity_to_location = inputs
        a = inputs.split('\n')
        humidity_to_location = '\n'.join(a[1:])

locs = []

def seed_mapping2(seed):
    for line in seed_to_soil.strip().split("\n"):
        m = re.match("([0-9]+)\s([0-9]+)\s([0-9]+)", line)
        destination_range_start = int(m.group(1))
        source_range_start = int(m.group(2))
        range_length = int(m.group(3))
        if source_range_start <= seed and seed <= source_range_start + range_length - 1:
            diff_between_destination_and_source = destination_range_start - source_range_start
            seed = seed + diff_between_destination_and_source
            break


    for line in soil_to_fertilizer.strip().split("\n"):
        m = re.match("([0-9]+)\s([0-9]+)\s([0-9]+)", line)
        destination_range_start = int(m.group(1))
        source_range_start = int(m.group(2))
        range_length = int(m.group(3))

        if source_range_start <= seed and seed <= source_range_start + range_length - 1:
            diff_between_destination_and_source = destination_range_start - source_range_start
            seed = seed + diff_between_destination_and_source
            break


    for line in fertilizer_to_water.strip().split("\n"):
        m = re.match("([0-9]+)\s([0-9]+)\s([0-9]+)", line)
        destination_range_start = int(m.group(1))
        source_range_start = int(m.group(2))
        range_length = int(m.group(3))

        if source_range_start <= seed and seed <= source_range_start + range_length - 1:
            diff_between_destination_and_source = destination_range_start - source_range_start
            seed = seed + diff_between_destination_and_source
            break


    for line in water_to_light.strip().split("\n"):
        m = re.match("([0-9]+)\s([0-9]+)\s([0-9]+)", line)
        destination_range_start = int(m.group(1))
        source_range_start = int(m.group(2))
        range_length = int(m.group(3))

        if source_range_start <= seed and seed <= source_range_start + range_length - 1:
            diff_between_destination_and_source = destination_range_start - source_range_start
            seed = seed + diff_between_destination_and_source
            break


    for line in light_to_temperature.strip().split("\n"):
        m = re.match("([0-9]+)\s([0-9]+)\s([0-9]+)", line)
        destination_range_start = int(m.group(1))
        source_range_start = int(m.group(2))
        range_length = int(m.group(3))

        if source_range_start <= seed and seed <= source_range_start + range_length - 1:
            diff_between_destination_and_source = destination_range_start - source_range_start
            seed = seed + diff_between_destination_and_source
            break


    for line in temperature_to_humidity.strip().split("\n"):
        m = re.match("([0-9]+)\s([0-9]+)\s([0-9]+)", line)
        destination_range_start = int(m.group(1))
        source_range_start = int(m.group(2))
        range_length = int(m.group(3))

        if source_range_start <= seed and seed <= source_range_start + range_length - 1:
            diff_between_destination_and_source = destination_range_start - source_range_start
            seed = seed + diff_between_destination_and_source
            break


    for line in humidity_to_location.strip().split("\n"):
        m = re.match("([0-9]+)\s([0-9]+)\s([0-9]+)", line)
        destination_range_start = int(m.group(1))
        source_range_start = int(m.group(2))
        range_length = int(m.group(3))

        if source_range_start <= seed and seed <= source_range_start + range_length - 1:
            diff_between_destination_and_source = destination_range_start - source_range_start
            seed = seed + diff_between_destination_and_source
            break


    return seed

for s in seeds:
    locs.append(seed_mapping2(s))

star1 = min(locs)

# star 2

part2_seeds = [515785082, 87905039, 2104518691, 503149843, 720333403, 385234193, 1357904101, 283386167, 93533455, 128569683, 2844655470, 24994629, 3934515023, 67327818, 2655687716, 8403417, 3120497449, 107756881, 4055128129, 9498708]

part2_seeds = [79, 14, 55, 13]



min_loc = 1000000000000000

for i in range(0,len(part2_seeds),2):
    range_start = part2_seeds[i]
    range_length = part2_seeds[i+1]
    # seeds = list(range(range_start, range_start+range_length))
    # print(seeds)
    # print(f'length of seeds {len(seeds)}')
    for s in range(range_start, range_start+range_length):
        # print(s)
        m = seed_mapping2(s)
        # print(m)
        if m < min_loc:
            min_loc = m

star2 = min_loc

print(f"star 1: {star1}")
print(f"star 2: {star2}")