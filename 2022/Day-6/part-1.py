file = "inputs.txt"
s = open(file, "r").read()[:-1]

l = list(s)

for a in range(len(s)):
    v = l[a:a+4]
    if len(set(v))==4:
        print(v)
        print(a+4)
        break
