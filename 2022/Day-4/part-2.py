file = "inputs.txt"
s = open(file, "r").read()[:-1]

a = [[[int(k) for k in j.split("-")] for j in i.split(",")]  for i in s.split("\n")]



b = [[set(range(x[0][0], x[0][1]+1)), set(range(x[1][0], x[1][1]+1))]  for x in a]

c = [len(list(f[1].intersection(f[0])))>0 for f in b]

print(sum(c))
