l = list(open("inputs.txt", "r").read())[:-1]


def path_calc(route):
    x = 0
    y = 0
    houses = []

    for i in route:
        match i:
            case ">":
                x += 1
            case "<":
                x -= 1
            case "^":
                y += 1
            case "v":
                y -= 1

        houses.append(str(x)+"x"+str(y))
    
    return houses


santa = path_calc(l[::2])
robot_santa = path_calc(l[1::2])

print(len(list(set(santa+robot_santa))))




