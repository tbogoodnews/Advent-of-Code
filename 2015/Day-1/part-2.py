s = open("inputs.txt", "r").read()

char = 0
floor = 0

print(list(s))

for i in list(s):
    char +=1
    print(i)
    if i == "(":
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        break 



