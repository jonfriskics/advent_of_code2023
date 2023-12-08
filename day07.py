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

# input = """
# QJJQ2 555
# """

def sort_and_count_cards(hand):
    h = {"2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "T": 0, "J": 0, "Q": 0, "K": 0, "A": 0}
    for c in hand:
        c = str(c)
        h[c] = h[c] + 1
    return h

card_order = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

hands_and_ranks = {}

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

def sort_hands_by_type(hand_type):
    cards_sorted_by_rank = []
    for hand in hand_type:
        cards_sorted_by_rank.append(convert_hand_to_numbered_list(hand))
    cards_sorted_by_rank = sorted(cards_sorted_by_rank, key=lambda x: x[4])
    cards_sorted_by_rank = sorted(cards_sorted_by_rank, key=lambda x: x[3])
    cards_sorted_by_rank = sorted(cards_sorted_by_rank, key=lambda x: x[2])
    cards_sorted_by_rank = sorted(cards_sorted_by_rank, key=lambda x: x[1])
    cards_sorted_by_rank = sorted(cards_sorted_by_rank, key=lambda x: x[0])
    return cards_sorted_by_rank

sorted_hands = []
sorted_hands = sorted_hands + sort_hands_by_type(high_card)
sorted_hands = sorted_hands + sort_hands_by_type(one_pair)
sorted_hands = sorted_hands + sort_hands_by_type(two_pair)
sorted_hands = sorted_hands + sort_hands_by_type(three_of_a_kind)
sorted_hands = sorted_hands + sort_hands_by_type(full_house)
sorted_hands = sorted_hands + sort_hands_by_type(four_of_a_kind)
sorted_hands = sorted_hands + sort_hands_by_type(five_of_a_kind)

r = 1
for h in sorted_hands:
    hand = convert_numbered_list_to_hand(h)
    hands_and_ranks[hand] = hands_and_ranks[hand] * r
    r += 1

star1 = sum(hands_and_ranks.values())

# star 2

def convert_hand_to_numbered_list2(hand):
    numbered_list = []
    for c in hand:
        if c == 'A':
            numbered_list.append(14)
        elif c == 'K':
            numbered_list.append(13)
        elif c == 'Q':
            numbered_list.append(12)
        elif c == 'J':
            numbered_list.append(1)
        elif c == 'T':
            numbered_list.append(10)
        else:
            numbered_list.append(int(c))
    return numbered_list

def convert_numbered_list_to_hand2(numbered_list):
    hand = ""
    for n in numbered_list:
        if n == 14:
            hand += "A"
        elif n == 13:
            hand += "K"
        elif n == 12:
            hand += "Q"
        elif n == 1:
            hand += "J"
        elif n == 10:
            hand += "T"
        else:
            hand += str(n)
    return hand

card_order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

hands_and_ranks = {}

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

def what_hand_is_this(hand):
    if 5 in hand.values():
        return "five_of_a_kind"
    elif 4 in hand.values():
        return "four_of_a_kind"
    elif 3 in hand.values() and 2 in hand.values():
        return "full_house"
    elif 3 in hand.values():
        return "three_of_a_kind"
    elif 2 in hand.values():
        ks = []
        for k, v in hand.items():
            if v == 2:
                ks.append(k)
        if len(ks) == 2:
            return "two_pair"
        elif len(ks) == 1:
            return "one_pair"
    else:
        return "high_card"

for line in input.strip().split("\n"):
    hand, bid = line.split(" ")
    hands_and_ranks[hand] = int(bid)
    sorted_and_counted_hand = sort_and_count_cards(hand)

    if sorted_and_counted_hand["J"] > 0:

        j_options = {}

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','A')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','K')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','Q')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','T')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','9')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','8')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','7')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','6')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','5')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','4')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','3')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        hand_to_replace = hand
        hand_to_replace = hand.replace('J','2')
        j_options[hand_to_replace] = what_hand_is_this(sort_and_count_cards(hand_to_replace))

        if 'five_of_a_kind' in j_options.values():
            five_of_a_kind.append(hand)
        elif 'four_of_a_kind' in j_options.values():
            four_of_a_kind.append(hand)
        elif 'full_house' in j_options.values():
            full_house.append(hand)
        elif 'three_of_a_kind' in j_options.values():
            three_of_a_kind.append(hand)
        elif 'two_pair' in j_options.values():
            two_pair.append(hand)
        elif 'one_pair' in j_options.values():
            one_pair.append(hand)
        elif 'high_card' in j_options.values():
            high_card.append(hand)
    else:
        if what_hand_is_this(sorted_and_counted_hand) == 'five_of_a_kind':
            five_of_a_kind.append(hand)
        elif what_hand_is_this(sorted_and_counted_hand) == 'four_of_a_kind':
            four_of_a_kind.append(hand)
        elif what_hand_is_this(sorted_and_counted_hand) == 'full_house':
            full_house.append(hand)
        elif what_hand_is_this(sorted_and_counted_hand) == 'three_of_a_kind':
            three_of_a_kind.append(hand)
        elif what_hand_is_this(sorted_and_counted_hand) == 'two_pair':
            two_pair.append(hand)
        elif what_hand_is_this(sorted_and_counted_hand) == 'one_pair':
            one_pair.append(hand)
        elif what_hand_is_this(sorted_and_counted_hand) == 'high_card':
            high_card.append(hand)

def sort_hands_by_type2(hand_type):
    cards_sorted_by_rank = []
    for hand in hand_type:
        cards_sorted_by_rank.append(convert_hand_to_numbered_list2(hand))
    cards_sorted_by_rank = sorted(cards_sorted_by_rank, key=lambda x: x[4])
    cards_sorted_by_rank = sorted(cards_sorted_by_rank, key=lambda x: x[3])
    cards_sorted_by_rank = sorted(cards_sorted_by_rank, key=lambda x: x[2])
    cards_sorted_by_rank = sorted(cards_sorted_by_rank, key=lambda x: x[1])
    cards_sorted_by_rank = sorted(cards_sorted_by_rank, key=lambda x: x[0])
    return cards_sorted_by_rank


sorted_hands = []
sorted_hands = sorted_hands + sort_hands_by_type2(high_card)
sorted_hands = sorted_hands + sort_hands_by_type2(one_pair)
sorted_hands = sorted_hands + sort_hands_by_type2(two_pair)
sorted_hands = sorted_hands + sort_hands_by_type2(three_of_a_kind)
sorted_hands = sorted_hands + sort_hands_by_type2(full_house)
sorted_hands = sorted_hands + sort_hands_by_type2(four_of_a_kind)
sorted_hands = sorted_hands + sort_hands_by_type2(five_of_a_kind)

r = 1
for h in sorted_hands:
    hand = convert_numbered_list_to_hand2(h)
    hands_and_ranks[hand] = hands_and_ranks[hand] * r
    r += 1

star2 = sum(hands_and_ranks.values())

print(f"star 1: {star1}")
print(f"star 2: {star2}")