file = "inputs.txt"

s = open(file, "r").read()[:-1].split("\n")

l = [[int(y) for y in x.split("\t")]for x in s]

print(sum([max(z)-min(z) for z in l]))




