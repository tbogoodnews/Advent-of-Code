file = "inputs.txt"
s = open(file, "r").read()[:-1].split("\n")

s = [[l.split(" ")[0], int(l.split(" ")[1]) ] for l in s]

pos = []

head = [0,0]
tail = [0,0]

directions = {"U" : [0,1], "D" : [0,-1], "L" : [-1, 0], "R" : [1, 0]}

for l in s:
    steps = 0
    d_s = directions[l[0]]
    print(l[1])
    for steps in range(l[1]):
        head = [head[0]+d_s[0], head[1]+d_s[1]]
        if tail[0]!=head[0] and tail[1]!=head[1]: # If on diagonal
            print("diagonal case")
            if abs(tail[0]-head[0])>1: # If there is a dist of more than to on x
                tail[1] = head[1] # Set the y coord to be equal
                tail[0] = (tail[0]+head[0])//2
            elif abs(tail[1]-head[1])>1:
                tail[0] = head[0]
                tail[1] = (tail[1]+head[1])//2
            else: # If stable diagonal
                pass
        else:
            if abs(tail[0]-head[0])>1: 
                tail[0] = (tail[0]+head[0])//2
            elif abs(tail[1]-head[1])>1:
                tail[1] = (tail[1]+head[1])//2
        print(head, tail)
        pos.append(str(tail[0]) + "x"+str(tail[1]))


print(len(set(pos)))

