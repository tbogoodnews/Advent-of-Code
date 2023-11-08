file = "inputs.txt"
s = [list(l) for l in open(file, "r").read()[:-1].split("\n")]

intersections = [list(set(s[i]) & set(s[i+1]) & set(s[i+2]))[0] for i in range(0,len(s),3)]

vals = [ord(v[0])-96 if ord(v[0])>96 else ord(v[0])-38 for v in intersections]

print(sum(vals))
