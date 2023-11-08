s = open("inputs.txt", "r").read()[:-1].split("\n")

s = [x.split(" ") for x in s]

print(sum([len(a)==len(set(a)) for a in s]))

