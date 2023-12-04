input_txt = open("input.txt")

data = [ l.split(": ")[1] for l in input_txt.read()[:-1].split("\n")]
data = [[v.split(" ")  for v in l.split(" | ")] for l in data]


def part_one(d):
    total = 0
    for l in d:
        nums = [int(i) for i in l[0] if i != ""]
        winning = [int(i) for i in l[1] if i != ""]
        temp = 0
        for n in nums:
            if n in winning:
                if temp == 0:
                    temp = 1
                else:
                    temp = temp * 2
        total += temp
    return total

def part_two(d):
    total = 0
    won_cards = list(range(1, len(d)+1))
    for x in range(1, 1 + len(d)):
        l = d[x-1]
        nums = [int(i) for i in l[0] if i != ""]
        winning = [int(i) for i in l[1] if i != ""]
        temp = 0
        for n in nums:
            if n in winning:
                temp += 1
        prev_seen = won_cards.count(x)
        won_cards += prev_seen * list( range (x+1, x + 1 + temp))
    return len(won_cards)



print("Solution to part one:", part_one(data))
print("Solution to part two:", part_two(data))
