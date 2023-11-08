file = "inputs.txt"
s = open(file, "r").read()[:-1]

l = list(s)

last_seen = []

print(len(l))

for a in range(len(s)):
    v = l[a:a+14]
    if len(set(v))==14:
        print(v)
        print(a+14)
        break
