s = open("inputs.txt", "r").read()

l = s.split("\n")[:-1]

total = 0

for i in l:
    l2 = i.split("x")
    length = int(l2[0])
    width = int(l2[1])
    height = int(l2[2])
    
    ribbon = (2*sum(sorted([length, width, height])[:2])) + (length*width*height)
    total += ribbon

print(total)
