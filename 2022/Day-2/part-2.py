s = open("inputs.txt").read()[:-1].split("\n")


# A = rock (1)
# B = paper (2)
# c = scissors (3)

# x = lose
# y = tie
# z = win

outcomes = {"A":{"X": 3, "Y" : 1, "Z" : 2}, 
            "B": {"X": 1, "Y" : 2, "Z" : 3}, 
            "C": {"X": 2, "Y" : 3, "Z" : 1}}

points = {"X":0, "Y": 3, "Z":6}

total = 0

for l in s:
    elf, me = l.split(" ")
    total += outcomes[elf][me] + points[me]

print(total)
