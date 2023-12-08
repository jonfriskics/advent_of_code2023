import os
import re

input = ''

day = re.search('\d+', os.path.basename(__file__)).group()

with open(f'inputs/input{day}.txt', 'r') as file:
    input = file.read()

star1 = 0
star2 = 0

# star 1

# input = """
# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# """

# input = """
# 23456 111
# """

card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

hands_and_ranks = {}

def sort_and_count_cards(hand):
    h = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "T": 0, "J": 0, "Q": 0, "K": 0, "A": 0}
    for c in hand:
        c = str(c)
        h[c] = h[c] + 1
    return h

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

for line in input.strip().split("\n"):
    hand, bid = line.split(" ")
    hands_and_ranks[hand] = int(bid)
    sorted_and_counted_hand = sort_and_count_cards(hand)
    if 5 in sorted_and_counted_hand.values():
        five_of_a_kind.append(hand)
    elif 4 in sorted_and_counted_hand.values():
        four_of_a_kind.append(hand)
    elif 3 in sorted_and_counted_hand.values() and 2 in sorted_and_counted_hand.values():
        full_house.append(hand)
    elif 3 in sorted_and_counted_hand.values():
        three_of_a_kind.append(hand)
    elif 2 in sorted_and_counted_hand.values():
        # either two pair or one pair
        ks = []
        for k, v in sorted_and_counted_hand.items():
            if v == 2:
                ks.append(k)
        if len(ks) == 2:
            two_pair.append(hand)
        elif len(ks) == 1:
            one_pair.append(hand)
    else:
        high_card.append(hand)

def convert_hand_to_numbered_list(hand):
    numbered_list = []
    for c in hand:
        if c == 'A':
            numbered_list.append(14)
        elif c == 'K':
            numbered_list.append(13)
        elif c == 'Q':
            numbered_list.append(12)
        elif c == 'J':
            numbered_list.append(11)
        elif c == 'T':
            numbered_list.append(10)
        else:
            numbered_list.append(int(c))
    return numbered_list

high_cards_sorted_by_rank = []
for hand in high_card:
    high_cards_sorted_by_rank.append(convert_hand_to_numbered_list(hand))
high_cards_sorted_by_rank = sorted(high_cards_sorted_by_rank, key=lambda x: x[4])
high_cards_sorted_by_rank = sorted(high_cards_sorted_by_rank, key=lambda x: x[3])
high_cards_sorted_by_rank = sorted(high_cards_sorted_by_rank, key=lambda x: x[2])
high_cards_sorted_by_rank = sorted(high_cards_sorted_by_rank, key=lambda x: x[1])
high_cards_sorted_by_rank = sorted(high_cards_sorted_by_rank, key=lambda x: x[0])

one_pair_sorted_by_rank = []
for hand in one_pair:
    one_pair_sorted_by_rank.append(convert_hand_to_numbered_list(hand))
one_pair_sorted_by_rank = sorted(one_pair_sorted_by_rank, key=lambda x: x[4])
one_pair_sorted_by_rank = sorted(one_pair_sorted_by_rank, key=lambda x: x[3])
one_pair_sorted_by_rank = sorted(one_pair_sorted_by_rank, key=lambda x: x[2])
one_pair_sorted_by_rank = sorted(one_pair_sorted_by_rank, key=lambda x: x[1])
one_pair_sorted_by_rank = sorted(one_pair_sorted_by_rank, key=lambda x: x[0])


two_pair_sorted_by_rank = []
for hand in two_pair:
    two_pair_sorted_by_rank.append(convert_hand_to_numbered_list(hand))
two_pair_sorted_by_rank = sorted(two_pair_sorted_by_rank, key=lambda x: x[4])
two_pair_sorted_by_rank = sorted(two_pair_sorted_by_rank, key=lambda x: x[3])
two_pair_sorted_by_rank = sorted(two_pair_sorted_by_rank, key=lambda x: x[2])
two_pair_sorted_by_rank = sorted(two_pair_sorted_by_rank, key=lambda x: x[1])
two_pair_sorted_by_rank = sorted(two_pair_sorted_by_rank, key=lambda x: x[0])

three_of_a_kind_sorted_by_rank = []
for hand in three_of_a_kind:
    three_of_a_kind_sorted_by_rank.append(convert_hand_to_numbered_list(hand))
three_of_a_kind_sorted_by_rank = sorted(three_of_a_kind_sorted_by_rank, key=lambda x: x[4])
three_of_a_kind_sorted_by_rank = sorted(three_of_a_kind_sorted_by_rank, key=lambda x: x[3])
three_of_a_kind_sorted_by_rank = sorted(three_of_a_kind_sorted_by_rank, key=lambda x: x[2])
three_of_a_kind_sorted_by_rank = sorted(three_of_a_kind_sorted_by_rank, key=lambda x: x[1])
three_of_a_kind_sorted_by_rank = sorted(three_of_a_kind_sorted_by_rank, key=lambda x: x[0])


full_house_sorted_by_rank = []
for hand in full_house:
    full_house_sorted_by_rank.append(convert_hand_to_numbered_list(hand))
full_house_sorted_by_rank = sorted(full_house_sorted_by_rank, key=lambda x: x[4])
full_house_sorted_by_rank = sorted(full_house_sorted_by_rank, key=lambda x: x[3])
full_house_sorted_by_rank = sorted(full_house_sorted_by_rank, key=lambda x: x[2])
full_house_sorted_by_rank = sorted(full_house_sorted_by_rank, key=lambda x: x[1])
full_house_sorted_by_rank = sorted(full_house_sorted_by_rank, key=lambda x: x[0])


four_of_a_kind_sorted_by_rank = []
for hand in four_of_a_kind:
    four_of_a_kind_sorted_by_rank.append(convert_hand_to_numbered_list(hand))
four_of_a_kind_sorted_by_rank = sorted(four_of_a_kind_sorted_by_rank, key=lambda x: x[4])
four_of_a_kind_sorted_by_rank = sorted(four_of_a_kind_sorted_by_rank, key=lambda x: x[3])
four_of_a_kind_sorted_by_rank = sorted(four_of_a_kind_sorted_by_rank, key=lambda x: x[2])
four_of_a_kind_sorted_by_rank = sorted(four_of_a_kind_sorted_by_rank, key=lambda x: x[1])
four_of_a_kind_sorted_by_rank = sorted(four_of_a_kind_sorted_by_rank, key=lambda x: x[0])


five_of_a_kind_sorted_by_rank = []
for hand in five_of_a_kind:
    four_of_a_kind_sorted_by_rank.append(convert_hand_to_numbered_list(hand))
five_of_a_kind_sorted_by_rank = sorted(five_of_a_kind_sorted_by_rank, key=lambda x: x[4])
five_of_a_kind_sorted_by_rank = sorted(five_of_a_kind_sorted_by_rank, key=lambda x: x[3])
five_of_a_kind_sorted_by_rank = sorted(five_of_a_kind_sorted_by_rank, key=lambda x: x[2])
five_of_a_kind_sorted_by_rank = sorted(five_of_a_kind_sorted_by_rank, key=lambda x: x[1])
five_of_a_kind_sorted_by_rank = sorted(five_of_a_kind_sorted_by_rank, key=lambda x: x[0])

def convert_numbered_list_to_hand(numbered_list):
    hand = ""
    for n in numbered_list:
        if n == 14:
            hand += "A"
        elif n == 13:
            hand += "K"
        elif n == 12:
            hand += "Q"
        elif n == 11:
            hand += "J"
        elif n == 10:
            hand += "T"
        else:
            hand += str(n)
    return hand

sorted_hands = []
sorted_hands = sorted_hands + high_cards_sorted_by_rank
sorted_hands = sorted_hands + one_pair_sorted_by_rank
sorted_hands = sorted_hands + two_pair_sorted_by_rank
sorted_hands = sorted_hands + three_of_a_kind_sorted_by_rank
sorted_hands = sorted_hands + full_house_sorted_by_rank
sorted_hands = sorted_hands + four_of_a_kind_sorted_by_rank
sorted_hands = sorted_hands + five_of_a_kind_sorted_by_rank

r = 1
for h in sorted_hands:
    hand = convert_numbered_list_to_hand(h)
    hands_and_ranks[hand] = hands_and_ranks[hand] * r
    r += 1

star1 = sum(hands_and_ranks.values())

# star 2

print(f"star 1: {star1}")
print(f"star 2: {star2}")