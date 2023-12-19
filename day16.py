import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

# input = r"""
# .|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|....
# """

def print_matrix(m):
  for l in range(len(m)):
    print(m[l])

star1 = []
star2 = []

# star 1

# matrix = []
# for i in input.strip().split("\n"):
#   l = list()
#   for s in i:
#     l.append(s)
#   matrix.append(l)

matrix = [list(line) for line in input.strip().splitlines()]

def still_active_beams(beams):
    for beam in beams:
        if beam['r_direction'] != 0 or beam['c_direction'] != 0:
            # print(f'    beam {beam["beam"]} still active')
            return True
    return False

def new_coordinate_in_matrix(r, c, matrix):
    max_row = len(matrix)
    max_col = len(matrix[0])
    if r >= 0 and r < max_row and c >= 0 and c < max_col:
        return True
    else:
        return False

beams = [{'beam': 1, 'r_position': 0, 'c_position': -1, 'r_direction': 0, 'c_direction': 1}]

last_30 = []
coords_touched_by_beam = set( )

while still_active_beams(beams):
    beams = [beam for beam in beams if not (beam['r_direction'] == 0 and beam['c_direction'] == 0)]
    max_beam = max(beams, key=lambda x: x['beam'])['beam']
    for beam in beams:
        # print(f'fbib {beam}')
        # look at one beam
        if beam['r_direction'] != 0 or beam['c_direction'] != 0:
            # print(f'beam {beam["beam"]} is still moving')
            current_r = beam['r_position']
            current_c = beam['c_position']
            if current_c != -1:
                coords_touched_by_beam.add((current_r, current_c))
                # print(f'coordinates seen: {sorted(list(coords_touched_by_beam))}')

            if beam['r_direction'] == 1:
                new_r = current_r + 1
                new_c = current_c + 0
                # print(f'beam {beam["beam"]} r_direction 1 --- new_r {new_r} new_c {new_c}')
                if new_coordinate_in_matrix(new_r, new_c, matrix):
                    if matrix[new_r][new_c] == '.':
                        # print(f'next char is .')

                        beam['r_position'] = new_r
                        beam['c_position'] = new_c
                        beam['r_direction'] = beam['r_direction']
                        beam['c_direction'] = beam['c_direction']
                    elif matrix[new_r][new_c] == '/':
                        # print(f'next char is /')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beam
                        new_k = max_beam + 1
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                    elif matrix[new_r][new_c] == '\\':
                        # print(f'next char is \\')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beam
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                    elif matrix[new_r][new_c] == '-':
                        # print(f'next char is -')

                        # print_matrix(matrix)
                        # print(f'[][][][][] {matrix[new_r][new_c]}')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beams
                        max_beam = max(beams, key=lambda x: x['beam'])['beam']
                        beams.append({'beam': max_beam+1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                        max_beam = max(beams, key=lambda x: x['beam'])['beam']
                        beams.append({'beam': max_beam+1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                        # print(f'beams after adding two {beams}')
                    elif matrix[new_r][new_c] == '|':
                        # print(f'next char is |')

                        beam['r_position'] = new_r
                        beam['c_position'] = new_c
                        beam['r_direction'] = beam['r_direction']
                        beam['c_direction'] = beam['c_direction']
                        # print(f'keep beam {beam["beam"]} going')
                else:
                    # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                    beam['r_direction'] = 0
                    beam['c_direction'] = 0
            elif beam['r_direction'] == -1:
                new_r = current_r - 1
                new_c = current_c + 0
                # print(f'beam {beam["beam"]} r_direction -1 --- new_r {new_r} new_c {new_c}')
                if new_coordinate_in_matrix(new_r, new_c, matrix):
                    if matrix[new_r][new_c] == '.':
                        # print(f'next char is .')

                        beam['r_position'] = new_r
                        beam['c_position'] = new_c
                        beam['r_direction'] = beam['r_direction']
                        beam['c_direction'] = beam['c_direction']
                    elif matrix[new_r][new_c] == '/':
                        # print(f'next char is /')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beam
                        new_k = max_beam + 1
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                    elif matrix[new_r][new_c] == '\\':
                        # print(f'next char is \\')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beam
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                    elif matrix[new_r][new_c] == '-':
                        # print(f'next char is -')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beams
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                        beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                    elif matrix[new_r][new_c] == '|':
                        # print(f'next char is |')

                        beam['r_position'] = new_r
                        beam['c_position'] = new_c
                        beam['r_direction'] = beam['r_direction']
                        beam['c_direction'] = beam['c_direction']
                        # print(f'keep beam {beam["beam"]} going')
                else:
                    # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                    beam['r_direction'] = 0
                    beam['c_direction'] = 0
            elif beam['c_direction'] == 1:
                new_r = current_r + 0
                new_c = current_c + 1
                # print(f'beam {beam["beam"]} c_direction 1 --- new_r {new_r} new_c {new_c}')
                if new_coordinate_in_matrix(new_r, new_c, matrix):
                    if matrix[new_r][new_c] == '.':
                        # print(f'next char is .')

                        beam['r_position'] = new_r
                        beam['c_position'] = new_c
                        beam['r_direction'] = beam['r_direction']
                        beam['c_direction'] = beam['c_direction']
                    elif matrix[new_r][new_c] == '/':
                        # print(f'next char is /')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beam
                        new_k = max_beam + 1
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                    elif matrix[new_r][new_c] == '\\':
                        # print(f'next char is \\')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beam
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})
                    elif matrix[new_r][new_c] == '-':
                        # print(f'next char is -')

                        beam['r_position'] = new_r
                        beam['c_position'] = new_c
                        beam['r_direction'] = 0
                        beam['c_direction'] = 1
                        # print(f'keep beam {beam["beam"]} going')

                        # start new beam
                        # beams[max(k)+1] = {'r_position': new_r, 'c_position': new_c, 'r_direction': , 'c_direction': 0}
                    elif matrix[new_r][new_c] == '|':
                        # print(f'next char is |')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beams
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                        beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})

                else:
                    # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                    beam['r_direction'] = 0
                    beam['c_direction'] = 0
            elif beam['c_direction'] == -1:
                new_r = current_r + 0
                new_c = current_c - 1
                # print(f'beam {beam["beam"]} c_direction -1 --- new_r {new_r} new_c {new_c}')
                if new_coordinate_in_matrix(new_r, new_c, matrix):
                    if matrix[new_r][new_c] == '.':
                        # print(f'next char is .')

                        beam['r_position'] = new_r
                        beam['c_position'] = new_c
                        beam['r_direction'] = beam['r_direction']
                        beam['c_direction'] = beam['c_direction']
                    elif matrix[new_r][new_c] == '/':
                        # print(f'next char is /')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beam
                        new_k = max_beam + 1
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})
                    elif matrix[new_r][new_c] == '\\':
                        # print(f'next char is \\')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beam
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                    elif matrix[new_r][new_c] == '-':
                        # print(f'next char is -')

                        # stop current beam
                        beam['r_position'] = new_r
                        beam['c_position'] = new_c
                        beam['r_direction'] = 0
                        beam['c_direction'] = -1
                        # print(f'keep beam {beam["beam"]} going')

                        # start new beam
                        # beams[max(k)+1] = {'r_position': new_r, 'c_position': new_c, 'r_direction': , 'c_direction': 0}
                    elif matrix[new_r][new_c] == '|':
                        # print(f'next char is |')

                        # stop current beam
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                        # print(f'kill beam {beam["beam"]}')

                        # start new beams
                        beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                        beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})

                else:
                    # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                    beam['r_direction'] = 0
                    beam['c_direction'] = 0

    # print(len(coords_touched_by_beam), len(beams))
    if len(last_30) < 30:
        last_30.append(len(coords_touched_by_beam))
    else:
        last_30 = last_30[1:]
        last_30.append(len(coords_touched_by_beam))
    if len(last_30) == 30 and all(n == last_30[0] for n in last_30):
        star1.append(len(coords_touched_by_beam))
        # print(f'len(coords_touched_by_beam) {len(coords_touched_by_beam)} {coords_touched_by_beam}')
        coords_touched_by_beam = set()
        last_30 = []
        # print(f'star1 {star1}')
        break
    else:
        pass #print(last_30)

print(max(star1))
exit()

# star 2

breaker = 0

last_30 = []
coords_touched_by_beam = set()

# left to right, start at 0, -1
# for i in range(len(matrix)):
#     beams = [{'beam': 1, 'r_position': i, 'c_position': -1, 'r_direction': 0, 'c_direction': 1}]
#     print(i, beams[0])
#     # if i == 3:
#     #     exit()
#     print(f'beams {beams}')

#     while still_active_beams(beams):
#         beams = [beam for beam in beams if not (beam['r_direction'] == 0 and beam['c_direction'] == 0)]
#         max_beam = max(beams, key=lambda x: x['beam'])['beam']
#         for beam in beams:
#             # print(f'fbib {beam}')
#             # look at one beam
#             if beam['r_direction'] != 0 or beam['c_direction'] != 0:
#                 # print(f'beam {beam["beam"]} is still moving')
#                 current_r = beam['r_position']
#                 current_c = beam['c_position']
#                 coords_touched_by_beam.add((current_r,current_c))
#                 if current_c != -1:
#                     print(f'current r {current_r} c {current_c}')
#                     coords_touched_by_beam.add((current_r, current_c))
#                     # print(f'coordinates seen: {sorted(list(coords_touched_by_beam))}')

#                 if beam['r_direction'] == 1:
#                     new_r = current_r + 1
#                     new_c = current_c + 0
#                     # print(f'beam {beam["beam"]} r_direction 1 --- new_r {new_r} new_c {new_c}')
#                     if new_coordinate_in_matrix(new_r, new_c, matrix):
#                         if matrix[new_r][new_c] == '.':
#                             # print(f'next char is .')

#                             beam['r_position'] = new_r
#                             beam['c_position'] = new_c
#                             beam['r_direction'] = beam['r_direction']
#                             beam['c_direction'] = beam['c_direction']
#                         elif matrix[new_r][new_c] == '/':
#                             # print(f'next char is /')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beam
#                             new_k = max_beam + 1
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
#                         elif matrix[new_r][new_c] == '\\':
#                             # print(f'next char is \\')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beam
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
#                         elif matrix[new_r][new_c] == '-':
#                             # print(f'next char is -')

#                             # print_matrix(matrix)
#                             # print(f'[][][][][] {matrix[new_r][new_c]}')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beams
#                             max_beam = max(beams, key=lambda x: x['beam'])['beam']
#                             beams.append({'beam': max_beam+1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
#                             max_beam = max(beams, key=lambda x: x['beam'])['beam']
#                             beams.append({'beam': max_beam+1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
#                             # print(f'beams after adding two {beams}')
#                         elif matrix[new_r][new_c] == '|':
#                             # print(f'next char is |')

#                             beam['r_position'] = new_r
#                             beam['c_position'] = new_c
#                             beam['r_direction'] = beam['r_direction']
#                             beam['c_direction'] = beam['c_direction']
#                             # print(f'keep beam {beam["beam"]} going')
#                     else:
#                         # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
#                         beam['r_direction'] = 0
#                         beam['c_direction'] = 0
#                 elif beam['r_direction'] == -1:
#                     new_r = current_r - 1
#                     new_c = current_c + 0
#                     # print(f'beam {beam["beam"]} r_direction -1 --- new_r {new_r} new_c {new_c}')
#                     if new_coordinate_in_matrix(new_r, new_c, matrix):
#                         if matrix[new_r][new_c] == '.':
#                             # print(f'next char is .')

#                             beam['r_position'] = new_r
#                             beam['c_position'] = new_c
#                             beam['r_direction'] = beam['r_direction']
#                             beam['c_direction'] = beam['c_direction']
#                         elif matrix[new_r][new_c] == '/':
#                             # print(f'next char is /')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beam
#                             new_k = max_beam + 1
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
#                         elif matrix[new_r][new_c] == '\\':
#                             # print(f'next char is \\')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beam
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
#                         elif matrix[new_r][new_c] == '-':
#                             # print(f'next char is -')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beams
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
#                             beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
#                         elif matrix[new_r][new_c] == '|':
#                             # print(f'next char is |')

#                             beam['r_position'] = new_r
#                             beam['c_position'] = new_c
#                             beam['r_direction'] = beam['r_direction']
#                             beam['c_direction'] = beam['c_direction']
#                             # print(f'keep beam {beam["beam"]} going')
#                     else:
#                         # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
#                         beam['r_direction'] = 0
#                         beam['c_direction'] = 0
#                 elif beam['c_direction'] == 1:
#                     new_r = current_r + 0
#                     new_c = current_c + 1
#                     # print(f'beam {beam["beam"]} c_direction 1 --- new_r {new_r} new_c {new_c}')
#                     if new_coordinate_in_matrix(new_r, new_c, matrix):
#                         if matrix[new_r][new_c] == '.':
#                             # print(f'next char is .')

#                             beam['r_position'] = new_r
#                             beam['c_position'] = new_c
#                             beam['r_direction'] = beam['r_direction']
#                             beam['c_direction'] = beam['c_direction']
#                         elif matrix[new_r][new_c] == '/':
#                             # print(f'next char is /')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beam
#                             new_k = max_beam + 1
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
#                         elif matrix[new_r][new_c] == '\\':
#                             # print(f'next char is \\')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beam
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})
#                         elif matrix[new_r][new_c] == '-':
#                             # print(f'next char is -')

#                             beam['r_position'] = new_r
#                             beam['c_position'] = new_c
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 1
#                             # print(f'keep beam {beam["beam"]} going')

#                             # start new beam
#                             # beams[max(k)+1] = {'r_position': new_r, 'c_position': new_c, 'r_direction': , 'c_direction': 0}
#                         elif matrix[new_r][new_c] == '|':
#                             # print(f'next char is |')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beams
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
#                             beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})

#                     else:
#                         # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
#                         beam['r_direction'] = 0
#                         beam['c_direction'] = 0
#                 elif beam['c_direction'] == -1:
#                     new_r = current_r + 0
#                     new_c = current_c - 1
#                     # print(f'beam {beam["beam"]} c_direction -1 --- new_r {new_r} new_c {new_c}')
#                     if new_coordinate_in_matrix(new_r, new_c, matrix):
#                         if matrix[new_r][new_c] == '.':
#                             # print(f'next char is .')

#                             beam['r_position'] = new_r
#                             beam['c_position'] = new_c
#                             beam['r_direction'] = beam['r_direction']
#                             beam['c_direction'] = beam['c_direction']
#                         elif matrix[new_r][new_c] == '/':
#                             # print(f'next char is /')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beam
#                             new_k = max_beam + 1
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})
#                         elif matrix[new_r][new_c] == '\\':
#                             # print(f'next char is \\')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beam
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
#                         elif matrix[new_r][new_c] == '-':
#                             # print(f'next char is -')

#                             # stop current beam
#                             beam['r_position'] = new_r
#                             beam['c_position'] = new_c
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = -1
#                             # print(f'keep beam {beam["beam"]} going')

#                             # start new beam
#                             # beams[max(k)+1] = {'r_position': new_r, 'c_position': new_c, 'r_direction': , 'c_direction': 0}
#                         elif matrix[new_r][new_c] == '|':
#                             # print(f'next char is |')

#                             # stop current beam
#                             beam['r_direction'] = 0
#                             beam['c_direction'] = 0
#                             # print(f'kill beam {beam["beam"]}')

#                             # start new beams
#                             beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
#                             beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})

#                     else:
#                         # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
#                         beam['r_direction'] = 0
#                         beam['c_direction'] = 0

#         # print(len(coords_touched_by_beam), len(beams))
#         if len(last_30) < 30:
#             last_30.append(len(coords_touched_by_beam))
#         else:
#             last_30 = last_30[1:]
#             last_30.append(len(coords_touched_by_beam))
#         if len(last_30) == 30 and all(n == last_30[0] for n in last_30):
#             star2.append(len(coords_touched_by_beam))
#             # print(f'len(coords_touched_by_beam) {len(coords_touched_by_beam)} {coords_touched_by_beam}')
#             print(coords_touched_by_beam)
#             coords_touched_by_beam = set()
#             last_30 = []
#             # print(f'star2 {star2}')
#             break
#         else:
#             pass #print(last_30)
#         # if len(coords_touched_by_beam) == 8112:
#         #     print(beams)
#             # break
#         # if breaker == 50:
#         #     print(f'breaker {breaker}')
#         #     break
#         # breaker += 1
#     # print(f'last_30 {last_30}')
#     if len(last_30) > 0:
#         star2.append(max(last_30))
#         coords_touched_by_beam = set ()
#     last_30 = []
#     # coords_touched_by_beam = set()

# print(star2)

last_30 = []

# print_matrix(matrix)

coords_touched_by_beam = set()

# right to left, start at 0, -1
for i in range(len(matrix)):
    beams = [{'beam': 1, 'r_position': i, 'c_position': len(matrix), 'r_direction': 0, 'c_direction': -1}]
    coords_touched_by_beam.add((i,len(matrix)-1))
    # print(i)
    if i == 3:
        exit()
    # print(f'beams {beams}')
    print(f'starting at {i} {len(matrix)}')
    while still_active_beams(beams):
        beams = [beam for beam in beams if not (beam['r_direction'] == 0 and beam['c_direction'] == 0)]
        max_beam = max(beams, key=lambda x: x['beam'])['beam']
        for beam in beams:
            # print(f'fbib {beam}')
            # look at one beam
            if beam['r_direction'] != 0 or beam['c_direction'] != 0:
                # print(f'beam {beam["beam"]} is still moving')
                current_r = beam['r_position']
                current_c = beam['c_position']
                # if current_c != len(matrix):
                coords_touched_by_beam.add((current_r, current_c))
                    # print(f'coordinates seen: {sorted(list(coords_touched_by_beam))}')
                # print(len(coords_touched_by_beam))

                if beam['r_direction'] == 1:
                    new_r = current_r + 1
                    new_c = current_c + 0
                    # print(f'{i} beam {beam["beam"]} r_direction 1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            # print_matrix(matrix)
                            # print(f'[][][][][] {matrix[new_r][new_c]}')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            max_beam = max(beams, key=lambda x: x['beam'])['beam']
                            beams.append({'beam': max_beam+1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                            max_beam = max(beams, key=lambda x: x['beam'])['beam']
                            beams.append({'beam': max_beam+1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                            # print(f'beams after adding two {beams}')
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                            # print(f'keep beam {beam["beam"]} going')
                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                elif beam['r_direction'] == -1:
                    new_r = current_r - 1
                    new_c = current_c + 0
                    # print(f'{i} beam {beam["beam"]} r_direction -1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                            beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                            # print(f'keep beam {beam["beam"]} going')
                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                elif beam['c_direction'] == 1:
                    new_r = current_r + 0
                    new_c = current_c + 1
                    # print(f'{i} beam {beam["beam"]} c_direction 1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = 0
                            beam['c_direction'] = 1
                            # print(f'keep beam {beam["beam"]} going')

                            # start new beam
                            # beams[max(k)+1] = {'r_position': new_r, 'c_position': new_c, 'r_direction': , 'c_direction': 0}
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                            beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})

                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                elif beam['c_direction'] == -1:
                    new_r = current_r + 0
                    new_c = current_c - 1
                    # print(f'{i} beam {beam["beam"]} c_direction -1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = 0
                            beam['c_direction'] = -1
                            # print(f'keep beam {beam["beam"]} going')

                            # start new beam
                            # beams[max(k)+1] = {'r_position': new_r, 'c_position': new_c, 'r_direction': , 'c_direction': 0}
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                            beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})

                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0

        # print(len(coords_touched_by_beam), len(beams))
        print(len(last_30), last_30, star2)
        if len(last_30) < 30:
            last_30.append(len(coords_touched_by_beam))
        else:
            last_30 = last_30[1:]
            last_30.append(len(coords_touched_by_beam))
        if len(last_30) == 30 and all(n == last_30[0] for n in last_30[:-10]):
            star2.append(len(coords_touched_by_beam))
            # print(f'len(coords_touched_by_beam) {len(coords_touched_by_beam)} {coords_touched_by_beam}')
            coords_touched_by_beam = set()
            last_30 = []
            # print(f'star2 {star2}')
            break
        else:
            pass #print(last_30)
        # if len(coords_touched_by_beam) == 8112:
        #     print(beams)
            # break
        # if breaker == 50:
        #     print(f'breaker {breaker}')
        #     break
        # breaker += 1
    # print(f'last_30 {last_30}')
    if len(last_30) > 0:
        star2.append(max(last_30))
    last_30 = []
    coords_touched_by_beam = set()
    print(f'{i} {star2}')

print(star2)
exit()

last_30 = []

# print_matrix(matrix)

coords_touched_by_beam = set()


# top to bottom, start from -1, 0
for i in range(len(matrix)):
    beams = [{'beam': 1, 'r_position': -1, 'c_position': i, 'r_direction': 1, 'c_direction': 0}]
    coords_touched_by_beam.add((0,i))
    # if i == 10:
    #     exit()
    # print(f'beams {beams}')

    while still_active_beams(beams):
        beams = [beam for beam in beams if not (beam['r_direction'] == 0 and beam['c_direction'] == 0)]
        max_beam = max(beams, key=lambda x: x['beam'])['beam']
        for beam in beams:
            # print(f'fbib {beam}')
            # look at one beam
            if beam['r_direction'] != 0 or beam['c_direction'] != 0:
                # print(f'beam {beam["beam"]} is still moving')
                current_r = beam['r_position']
                current_c = beam['c_position']
                if current_r != -1:
                    coords_touched_by_beam.add((current_r, current_c))
                    # print(f'coordinates seen: {sorted(list(coords_touched_by_beam))}')

                if beam['r_direction'] == 1:
                    new_r = current_r + 1
                    new_c = current_c + 0
                    # print(f'beam {beam["beam"]} r_direction 1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            # print_matrix(matrix)
                            # print(f'[][][][][] {matrix[new_r][new_c]}')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            max_beam = max(beams, key=lambda x: x['beam'])['beam']
                            beams.append({'beam': max_beam+1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                            max_beam = max(beams, key=lambda x: x['beam'])['beam']
                            beams.append({'beam': max_beam+1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                            # print(f'beams after adding two {beams}')
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                            # print(f'keep beam {beam["beam"]} going')
                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                elif beam['r_direction'] == -1:
                    new_r = current_r - 1
                    new_c = current_c + 0
                    # print(f'beam {beam["beam"]} r_direction -1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                            beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                            # print(f'keep beam {beam["beam"]} going')
                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                elif beam['c_direction'] == 1:
                    new_r = current_r + 0
                    new_c = current_c + 1
                    # print(f'beam {beam["beam"]} c_direction 1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = 0
                            beam['c_direction'] = 1
                            # print(f'keep beam {beam["beam"]} going')

                            # start new beam
                            # beams[max(k)+1] = {'r_position': new_r, 'c_position': new_c, 'r_direction': , 'c_direction': 0}
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                            beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})

                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                elif beam['c_direction'] == -1:
                    new_r = current_r + 0
                    new_c = current_c - 1
                    # print(f'beam {beam["beam"]} c_direction -1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            # stop current beam
                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = 0
                            beam['c_direction'] = -1
                            # print(f'keep beam {beam["beam"]} going')

                            # start new beam
                            # beams[max(k)+1] = {'r_position': new_r, 'c_position': new_c, 'r_direction': , 'c_direction': 0}
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                            beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})

                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0

        # print(len(coords_touched_by_beam), len(beams))
        if len(last_30) < 30:
            last_30.append(len(coords_touched_by_beam))
        else:
            last_30 = last_30[1:]
            last_30.append(len(coords_touched_by_beam))
        if len(last_30) == 30 and all(n == last_30[0] for n in last_30):
            star2.append(len(coords_touched_by_beam))
            # print(f'len(coords_touched_by_beam) {len(coords_touched_by_beam)} {coords_touched_by_beam}')
            coords_touched_by_beam = set()
            last_30 = []
            # print(f'star2 {star2}')
            break
        else:
            pass #print(last_30)
        # if len(coords_touched_by_beam) == 8112:
        #     print(beams)
            # break
        # if breaker == 50:
        #     print(f'breaker {breaker}')
        #     break
        # breaker += 1
    # print(f'last_30 {last_30}')
    if len(last_30) > 0:
        star2.append(max(last_30))
    last_30 = []
    coords_touched_by_beam = set()

print(star2)

coords_touched_by_beam = set()
last_30 = []

# bottom to top, start from max_row+1, 0
for i in range(len(matrix)):
    beams = [{'beam': 1, 'r_position': len(matrix), 'c_position': i, 'r_direction': -1, 'c_direction': 0}]
    coords_touched_by_beam.add((len(matrix)-1,i))
    # if i == 10:
    #     exit()
    # print(f'beams {beams}')

    while still_active_beams(beams):
        beams = [beam for beam in beams if not (beam['r_direction'] == 0 and beam['c_direction'] == 0)]
        max_beam = max(beams, key=lambda x: x['beam'])['beam']
        for beam in beams:
            # print(f'fbib {beam}')
            # look at one beam
            if beam['r_direction'] != 0 or beam['c_direction'] != 0:
                # print(f'beam {beam["beam"]} is still moving')
                current_r = beam['r_position']
                current_c = beam['c_position']
                if current_r != -1:
                    coords_touched_by_beam.add((current_r, current_c))
                    # print(f'coordinates seen: {sorted(list(coords_touched_by_beam))}')

                if beam['r_direction'] == 1:
                    new_r = current_r + 1
                    new_c = current_c + 0
                    # print(f'beam {beam["beam"]} r_direction 1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            # print_matrix(matrix)
                            # print(f'[][][][][] {matrix[new_r][new_c]}')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            max_beam = max(beams, key=lambda x: x['beam'])['beam']
                            beams.append({'beam': max_beam+1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                            max_beam = max(beams, key=lambda x: x['beam'])['beam']
                            beams.append({'beam': max_beam+1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                            # print(f'beams after adding two {beams}')
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                            # print(f'keep beam {beam["beam"]} going')
                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                elif beam['r_direction'] == -1:
                    new_r = current_r - 1
                    new_c = current_c + 0
                    # print(f'beam {beam["beam"]} r_direction -1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': 1})
                            beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 0, 'c_direction': -1})
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                            # print(f'keep beam {beam["beam"]} going')
                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                elif beam['c_direction'] == 1:
                    new_r = current_r + 0
                    new_c = current_c + 1
                    # print(f'beam {beam["beam"]} c_direction 1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = 0
                            beam['c_direction'] = 1
                            # print(f'keep beam {beam["beam"]} going')

                            # start new beam
                            # beams[max(k)+1] = {'r_position': new_r, 'c_position': new_c, 'r_direction': , 'c_direction': 0}
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                            beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})

                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0
                elif beam['c_direction'] == -1:
                    new_r = current_r + 0
                    new_c = current_c - 1
                    # print(f'beam {beam["beam"]} c_direction -1 --- new_r {new_r} new_c {new_c}')
                    if new_coordinate_in_matrix(new_r, new_c, matrix):
                        if matrix[new_r][new_c] == '.':
                            # print(f'next char is .')

                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = beam['r_direction']
                            beam['c_direction'] = beam['c_direction']
                        elif matrix[new_r][new_c] == '/':
                            # print(f'next char is /')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            new_k = max_beam + 1
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '\\':
                            # print(f'next char is \\')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beam
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                        elif matrix[new_r][new_c] == '-':
                            # print(f'next char is -')

                            # stop current beam
                            beam['r_position'] = new_r
                            beam['c_position'] = new_c
                            beam['r_direction'] = 0
                            beam['c_direction'] = -1
                            # print(f'keep beam {beam["beam"]} going')

                            # start new beam
                            # beams[max(k)+1] = {'r_position': new_r, 'c_position': new_c, 'r_direction': , 'c_direction': 0}
                        elif matrix[new_r][new_c] == '|':
                            # print(f'next char is |')

                            # stop current beam
                            beam['r_direction'] = 0
                            beam['c_direction'] = 0
                            # print(f'kill beam {beam["beam"]}')

                            # start new beams
                            beams.append({'beam': max_beam + 1, 'r_position': new_r, 'c_position': new_c, 'r_direction': -1, 'c_direction': 0})
                            beams.append({'beam': max_beam + 2, 'r_position': new_r, 'c_position': new_c, 'r_direction': 1, 'c_direction': 0})

                    else:
                        # print(f'-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- kill beam {beam["beam"]}')
                        beam['r_direction'] = 0
                        beam['c_direction'] = 0

        # print(len(coords_touched_by_beam), len(beams))
        if len(last_30) < 30:
            last_30.append(len(coords_touched_by_beam))
        else:
            last_30 = last_30[1:]
            last_30.append(len(coords_touched_by_beam))
        if len(last_30) == 30 and all(n == last_30[0] for n in last_30):
            star2.append(len(coords_touched_by_beam))
            # print(f'len(coords_touched_by_beam) {len(coords_touched_by_beam)} {coords_touched_by_beam}')
            coords_touched_by_beam = set()
            last_30 = []
            # print(f'star2 {star2}')
            break
        else:
            pass #print(last_30)
        # if len(coords_touched_by_beam) == 8112:
        #     print(beams)
            # break
        # if breaker == 50:
        #     print(f'breaker {breaker}')
        #     break
        # breaker += 1
    # print(f'last_30 {last_30}')
    if len(last_30) > 0:
        star2.append(max(last_30))
    last_30 = []
    coords_touched_by_beam = set()

print(star2)

print(f"star 1: {max(star1)}")
print(f"star 2: {max(star2)}")