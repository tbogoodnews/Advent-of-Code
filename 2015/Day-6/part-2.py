file = "inputs.txt"
s = open(file, "r").read()[:-1].split("\n")


lit = [[0 for j in range(1000)] for i in range(1000)]

for i in s:
    line = i.split(" through ")
    instruction, start = line[0].rsplit(" ", 1)
    start_x, start_y = start.split(",")
    end_x, end_y = line[1].split(",")
    start_x, start_y, end_x, end_y = int(start_x), int(start_y), int(end_x), int(end_y)
    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            match instruction:
                case "turn on":
                    lit[y][x] += 1
                case "turn off":
                    lit[y][x] = max(lit[y][x]-1, 0)
                case "toggle":
                    lit[y][x] += 2

print(sum([sum(i) for i in lit]))

