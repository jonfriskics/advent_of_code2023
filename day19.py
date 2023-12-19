import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

input = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

star1 = 0
star2 = 0

workflows = input.split('\n\n')[0].strip()
ratings = input.split('\n\n')[1].strip()

wfs = {}
for workflow in workflows.split('\n'):
    match = re.match('(\w+)\{(.+)\}', workflow)
    wf_name = match.group(1)
    wf_rules = match.group(2)
    rules = wf_rules.split(',')

    wfs[wf_name] = {}

    r = 1
    for rule in rules:
        if rule.find(':') != -1:
            wfs[wf_name][r] = {'condition': rule.split(':')[0], 'to': rule.split(':')[1]}
        else:
            wfs[wf_name][r] = {'condition': None, 'to': rule}
        r += 1

for rating in ratings.split('\n'):
    match = re.match('{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}', rating)
    x = int(match.group(1))
    m = int(match.group(2))
    a = int(match.group(3))
    s = int(match.group(4))
    vals = {'x': x, 'm': m, 'a': a, 's': s}

    to = 'in'

    while to != None:
        if to == 'A':
            for k, v in vals.items():
                star1 += v
            # print(star1)
            break
        if to == 'R':
            break
        current_rule = wfs[to]
        for n in range(1,len(current_rule)+1):
            condition = current_rule[n]['condition']
            if condition == None:
                if current_rule[n]['to'] == 'A':
                    to = 'A'
                elif current_rule[n]['to'] == 'R':
                    to = None
                    break
                else:
                    to = current_rule[n]['to']
                    break
            elif condition.find('>') != -1 or condition.find('<') != -1:
                ma = re.match('([xmas])([\<\>])(\d+)', condition)
                letter = ma.group(1)
                direction = ma.group(2)
                number = int(ma.group(3))

                if direction == '<':
                    if vals[letter] < number:
                        to = current_rule[n]['to']
                        break
                    else:
                        continue
                elif direction == '>':
                    if vals[letter] > number:
                        to = current_rule[n]['to']
                        break
                    else:
                        continue

print('star1', star1)

# too slow!
for x in range(1,4001):
    for m in range(1, 4001):
        for a in range(1, 4001):
            for s in range(1, 4001):
                vals = {'x': x, 'm': m, 'a': a, 's': s}

                to = 'in'

                while to != None:
                    if to == 'A':
                        star2 += 1
                        break
                    if to == 'R':
                        break
                    current_rule = wfs[to]
                    for n in range(1,len(current_rule)+1):
                        condition = current_rule[n]['condition']
                        if condition == None:
                            if current_rule[n]['to'] == 'A':
                                to = 'A'
                            elif current_rule[n]['to'] == 'R':
                                to = None
                                break
                            else:
                                to = current_rule[n]['to']
                                break
                        elif condition.find('>') != -1 or condition.find('<') != -1:
                            ma = re.match('([xmas])([\<\>])(\d+)', condition)
                            letter = ma.group(1)
                            direction = ma.group(2)
                            number = int(ma.group(3))

                            if direction == '<':
                                if vals[str(letter)] < number:
                                    to = current_rule[n]['to']
                                    break
                                else:
                                    continue
                            elif direction == '>':
                                if vals[str(letter)] > number:
                                    to = current_rule[n]['to']
                                    break
                                else:
                                    continue
                break # comment out to run
            break # comment out to run
        break # comment out to run
    break # comment out to run

# star 1
# star 2

print(f"star 1: {star1}")
print(f"star 2: {star2}")