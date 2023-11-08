s = open("inputs.txt").read()[:-1].split("\n")

outcomes = {"A":{"X": 3, "Y" : 6, "Z" : 0}, 
            "B": {"X": 0, "Y" : 3, "Z" : 6}, 
            "C": {"X": 6, "Y" : 0, "Z" : 3}}

points = {"X":1, "Y": 2, "Z":3}

total = 0

for l in s:
    elf, me = l.split(" ")
    total += outcomes[elf][me] + points[me]

print(total)
