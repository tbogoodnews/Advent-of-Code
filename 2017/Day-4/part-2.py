s = open("inputs.txt", "r").read()[:-1].split("\n")

s = [x.split(" ") for x in s]

print(sum([sum([a[b][::-1] in a[:b] + a[b+1:] for b in range(len(a))])==0 for a in s]))

