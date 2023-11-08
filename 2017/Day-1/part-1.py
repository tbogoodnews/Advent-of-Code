file = "inputs.txt"
s = list(open(file, "r").read()[:-1])


total = 0


for i in range(-1, len(s)-1):
    if s[i]==s[i+1]:
        total += int(s[i])

print(total)
