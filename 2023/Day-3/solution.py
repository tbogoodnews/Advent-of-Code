input_txt = open("input.txt")

data = input_txt.read()[:-1].split("\n")

def part_one(d):
    interesting_pos = set()
    for y in range(len(d)):
        for x in range(len(d[y])):
            if d[y][x] != "." and not d[y][x].isdigit():
                interesting_pos.add(tuple([x,y]))
    while True:
        temp = list(interesting_pos)
        max_x = len(d[0]) - 1
        max_y = len(d) - 1
        for v in temp:
            x = v[0]
            y = v[1]
            up = max(0,y-1)
            down = min(max_y,y+1)
            left = min(x+1, max_x)
            right = max(0, x-1)
            if d[up][x] != ".": # direct above
                interesting_pos.add(tuple([x,up]))
            if d[down][x] != ".": # direct below
                interesting_pos.add(tuple([x,down]))
            if d[y][right] != ".": # right
                interesting_pos.add(tuple([right,y]))
            if d[y][left] != ".": # left
                interesting_pos.add(tuple([left,y]))
            if d[up][right] != ".": # top right
                interesting_pos.add(tuple([right,up]))
            if d[up][left] != ".": # top left
                interesting_pos.add(tuple([left, up]))
            if d[down][right] != ".": # bottom right
                interesting_pos.add(tuple([right, down]))
            if d[down][left] != ".": # bottom left
                interesting_pos.add(tuple([left, down]))


        if len(interesting_pos) == len(temp):
            break
        else:
            len_interest = len(interesting_pos)
    total = 0
    for y in range(len(d)):
        l = d[y]
        pos_str = ""
        for x in range(len(l)):
            if tuple([x,y]) in interesting_pos:
                if l[x].isdigit():
                    if tuple([x-1,y]) not in interesting_pos and pos_str != "":
                        total += int(pos_str)
                        pos_str = ""
                    pos_str += l[x]
                elif pos_str != "":
                    total += int(pos_str)
                    pos_str = ""
        if pos_str != "":
            total += int(pos_str)
    return total


def part_two(d):
    gears = set()
    for y in range(len(d)):
        for x in range(len(d[y])):
            if d[y][x] == "*":
                gears.add(tuple([x,y]))
    total = 0
    print(len(gears))
    for g in gears:
        nums = []

        # search left
        temp = ""
        x = g[0] - 1
        y = g[1]
        while x >= 0: 
            if d[y][x].isdigit():
                temp = d[y][x] + temp
                x -= 1
            else:
                break
        if temp != "": nums.append(int(temp))
        
        # search righ
        temp = ""
        x = g[0] + 1
        y = g[1]
        while x < len(d[y]): # search right
            if d[y][x].isdigit():
                temp += d[y][x] 
                x += 1
            else:
                break
        if temp != "": nums.append(int(temp))

        # Search above
        if g[1] > 0:
            temp = ""
            y = g[1] -1
            x = g[0]
            if x-1 >= 0: #search leftwards
                x = x-1
                while x >= 0:
                    if d[y][x].isdigit():
                        temp = d[y][x] + temp
                        x -= 1
                    else:
                        break
            if d[y][g[0]].isdigit(): #check up middle
                temp += d[y][g[0]]
            else:
                if temp != "": 
                    nums.append(int(temp))
                    temp = "" # reset for next look
            x = g[0]
            if x+1 < len(d[y]): #search rightwards
                x = x+1
                while x < len(d[y]):
                    if d[y][x].isdigit():
                        temp = temp + d[y][x]
                        x += 1
                    else:
                        break
            if temp != "": nums.append(int(temp))
    
        # Search below
        if g[1] != len(d) -1:
            temp = ""
            y = g[1] + 1
            x = g[0]
            if x-1 >= 0: #search leftwards
                x = x-1
                while x >= 0:
                    if d[y][x].isdigit():
                        temp = d[y][x] + temp
                        x -= 1
                    else:
                        break
            if d[y][g[0]].isdigit(): #check up middle
                temp += d[y][g[0]]
            else:
                if temp != "":
                    nums.append(int(temp))
                    temp = "" # reset for next look
            x = g[0]
            if x+1 < len(d[y]): #search rightwards
                x = x+1
                while x < len(d[y]):
                    if d[y][x].isdigit():
                        temp = temp + d[y][x]
                        x += 1
                    else:
                        break
            if temp != "": nums.append(int(temp))

        if len(nums) == 2:
            total += nums[0] * nums[1]
    return total 

print("Solution to part one:", part_one(data))
print("Solution to part two:", part_two(data))
