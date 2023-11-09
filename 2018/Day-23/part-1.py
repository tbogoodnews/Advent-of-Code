f = open("input.txt").readlines()[:-1]

class Bot:
    def __init__(self, s):
        s = s[5:].split(">, r=") 
        pos = s[0].split(",")
        self.x = int(pos[0])
        self.y = int(pos[1])
        self.z = int(pos[2])
        self.radius = int(s[1])

def dist(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y) +  abs(a.z - b.z)

bots = [Bot(l) for l in f]
bots.sort(key = lambda x : x.radius)
max_bot = bots[-1]

distances = [dist(max_bot, j) for j in bots]

print("Number of bots in range:", sum(v <= max_bot.radius for v in distances) )


