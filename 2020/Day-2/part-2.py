import re

file = "inputs.txt"

s = open(file, "r").read()[:-1].split("\n")

a = [x.split(": ") for x in s]

b = [y[1].count(y[0][-1]) for y in a]

c = [re.split("-| ", z[0]) for z in a]

total = 0

for j in range(len(c)):
    print(a[j])
    
    i0 = a[j][1][int(c[j][0])-1]
    i1 = a[j][1][int(c[j][1])-1]
    t = a[j][0][-1]
    total += (i1==t) ^ (i0==t)

print(total)
