input_txt = open("input.txt")
data = [h.split() for h in input_txt.read()[:-1].split("\n")]

def eval_hand(h):
    cards = set(h)
    counts = [h.count(c) for c in list(h)]
    if len(cards) == 1:
        return 1 # "Five of a kind"
    if len(cards) == 2:
        if 4 in counts:
            return 2 # "Four of a kind"
        else:
            return 3 # "Full house"
    if len(cards) == 3:
        if 3 in counts:
            return 4 # "Three of a kind"
        else: 
            return 5 # "Two pair"
    if 2 in counts:
        return 6 # "One pair"
    return 7 # "High card"

card_value_one = "AKQJT98765432"
card_value_two = "AKQT98765432J"

def inter_hand(hands, card_value = card_value_one):
        ordered = sorted([z[0] for z in hands], key = lambda x : [card_value.index(c) for c in x])
        return sorted(hands, key = lambda x : ordered.index(x[0]))

def part_one(hands):
    temp = []
    for i in range(1,8):
        temp += inter_hand([c for c in hands if eval_hand(c[0]) == i])

    return sum((len(hands)-i) * int(temp[i][1])  for i in range(len(hands)))

def eval_hand_two(h):
    if "J" not in h:
        return eval_hand(h)
    return min(eval_hand(h.replace("J", c)) for c in card_value_two[:-1])

def part_two(hands):
    temp = []
    for i in range(1,8):
        temp += inter_hand([c for c in hands if eval_hand_two(c[0]) == i], card_value_two)

    return sum((len(hands)-i) * int(temp[i][1])  for i in range(len(hands)))

print("Solution to part one:", part_one(data))
print("Solution to part two:", part_two(data))
