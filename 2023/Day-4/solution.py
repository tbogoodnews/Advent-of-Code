import re
input_txt = open("input.txt")

data = [ l.split(": ")[1] for l in input_txt.read()[:-1].split("\n")]
data = [[re.findall(r'(\d+)', v)  for v in l.split(" | ")] for l in data]
matches = [ sum(n in l[1] for n in l[0]) for l in data ]

def part_one(d):
    return sum( 2**(x - 1) for x in d if x != 0) 

def part_two(d):
    won_cards = len(d)*[1] 
    for x in range(len(d)):
        for y in range (x+1, x+1 + d[x]):
            won_cards[y] += won_cards[x]
    return sum(won_cards)

print("Solution to part one:", part_one(matches))
print("Solution to part two:", part_two(matches))
