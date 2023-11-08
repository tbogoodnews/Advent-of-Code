l = list(open("inputs.txt", "r").read())[:-1]

x = 0
y = 0

spots = []

for i in l:
    match i:
        case ">":
            x += 1
        case "<":
            x -= 1
        case "^":
            y += 1
        case "v":
            y -= 1

    if [x,y] not in spots:
        spots.append([x,y])

print(len(spots)+1)


