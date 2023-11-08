import re

file = "inputs.txt"

s = open(file, "r").read()[:-1].split("\n")

a = [x.split(": ") for x in s]

b = [y[1].count(y[0][-1]) for y in a]

c = [re.split("-| ", z[0]) for z in a]

d = [int(c[j][1]) >=b[j] and int(c[j][0])<=b[j]  for j in range(len(c))]

print(sum(d))
