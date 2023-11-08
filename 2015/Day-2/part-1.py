s = open("inputs.txt", "r").read()

l = s.split("\n")[:-1]

total = 0

for i in l:
    l2 = i.split("x")
    length = int(l2[0])
    width = int(l2[1])
    height = int(l2[2])
    
    base = width*length
    side1 = width*height
    side2 = length*height

    present = (2*base) +(2*side1) + (2*side2) + min(base, side1, side2)
    total += present

print(total)
