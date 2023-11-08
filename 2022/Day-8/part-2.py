file = "inputs.txt"
s = open(file, "r").read()[:-1].split("\n")
s = [[int(l[x]) for x in range(len(l))] for l in s]
t = [[row[i] for row in s] for i in range(len(s[0]))]

max_visible =  0 

def len_viz(l, v):
    c = 0
    for i in l:
        c+=1
        if i>=v:
            return c
    return c

for y in range(1, len(s)-1):
    for x in range(1, len(s[y])-1):
        val = s[y][x]
        above = t[x][:y][::-1]
        av = len_viz(above, val)
        below = t[x][y+1:]
        bv = len_viz(below, val)
        left =  s[y][:x][::-1]
        lv = len_viz(left, val)
        right = s[y][x+1:]
        rv = len_viz(right, val)
        
        max_visible = max(max_visible, (av* bv* lv* rv))


print(max_visible)

