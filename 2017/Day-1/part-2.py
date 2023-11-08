file = "inputs.txt"
s = list(open(file, "r").read()[:-1])


total = 0
skip = len(s)/2

for i in range(0, len(s)-1):
    if s[i]==s[int((i+skip)%len(s))]:
        total += int(s[i])

print(total)
