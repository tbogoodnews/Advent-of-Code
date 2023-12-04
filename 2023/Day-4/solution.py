input_txt = open("input.txt")

data = [ l.split(": ")[1] for l in input_txt.read()[:-1].split("\n")]
data = [[v.split(" ")  for v in l.split(" | ")] for l in data]
matches = [ sum(n in [int(i) for i in l[1] if i != ""] for n in [int(i) for i in l[0] if i != ""]) for l in data ]

def part_one(d):
    return sum( 2**(x - 1) for x in d if x != 0) 

def part_two(d):
    won_cards = list(range(1, len(d)+1))
    for x in range(1, 1 + len(d)):
        won_cards += won_cards.count(x) * list( range (x+1, x + 1 + d[x-1]))
    return len(won_cards)

print("Solution to part one:", part_one(matches))
print("Solution to part two:", part_two(matches))
