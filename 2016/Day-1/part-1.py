file = "inputs.txt"

s = open(file, "r").read()[:-1].split(", ")

x = 0
y = 0

facing = "n"
directions = {  "n": {"L":"w", "R":"e"},
                "s": {"L":"e", "R":"w"},
                "e": {"L":"n", "R":"s"},
                "w": {"L":"s", "R":"n"}
}

for i in s:
    shift = i[0]
    facing = directions[facing][shift]
    move = int(i[1])
    print(i +":", shift, facing, move)
    match facing:
        case "n":
            y += move
        case "s":
            y -= move
        case "e":
            x += move
        case "w":
            x -= move
    print("(", x, y, ")")    
print(abs(x)+abs(y))
