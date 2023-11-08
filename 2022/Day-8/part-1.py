file = "inputs.txt"
s = open(file, "r").read()[:-1].split("\n")
s = [[int(l[x]) for x in range(len(l))] for l in s]
t = [[row[i] for row in s] for i in range(len(s[0]))]

visible = (2*len(s))+(2*(len(s[0])-2))

for y in range(1, len(s)-1):
    for x in range(1, len(s[y])-1):
        above = (s[y][x] > max(t[x][:y]))
        below = (s[y][x] > max(t[x][y+1:]))
        left =  (s[y][x] > max(s[y][:x]))
        right = (s[y][x] > max(s[y][x+1:]))
        visible +=  above or below or left or right

print(visible)

