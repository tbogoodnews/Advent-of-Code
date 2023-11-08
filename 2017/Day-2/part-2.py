file = "inputs.txt"

s = open(file, "r").read()[:-1].split("\n")

l = [[int(y) for y in x.split("\t")]for x in s]

total = 0

def gcd(r):
    for i in range(len(r)):
        for j in range(i+1, len(r)):
            if r[i]//r[j]==r[i]/r[j]:
                return r[i]//r[j]
    return 0

for i in l:
    total += max(gcd(i), gcd(i[::-1]))

print(total)



