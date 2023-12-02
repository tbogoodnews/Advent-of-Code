input_txt = open("input.txt")

class Game:
    def __init__(self, s):
        self.game_num = int(s.split(":")[0][5:])
        games = []
        for g in s.split(": ")[1].split("; "):
            d = dict()
            for x in g.split(", "):
                d[x.split(" ")[1]] = int(x.split(" ")[0])
            games.append(d)
        self.games = games
            
    def count_colours(self):
        red = sum(y["red"] for y in self.games if "red" in y.keys())
        green = sum(y["green"] for y in self.games if "green" in y.keys())
        blue = sum(y["blue"] for y in self.games if "blue" in y.keys())
        return [red, green, blue]
    
    def possible(self):
        for g in self.games:
            if "red" in g.keys():
                if g["red"] > 12:
                    return False
            if "green" in g.keys():
                if g["green"] > 13:
                    return False
            if "blue" in g.keys():
                if g["blue"] > 14:
                    return False
        return True

    def min_cubes(self):
        red = 0
        green = 0
        blue = 0
        for g in self.games:
            if "red" in g.keys():
                if g["red"] > red:
                    red = g["red"]
            if "green" in g.keys():
                if g["green"] > green:
                    green = g["green"]
            if "blue" in g.keys():
                if g["blue"] > blue:
                    blue = g["blue"]
        return red * green * blue

data = input_txt.read()[:-1].split("\n")
data = [Game(l) for l in data]

def part_one(s):
    sum_ids = 0
    for i in data:
        if i.possible():
            sum_ids += i.game_num
    return sum_ids


def part_two(s):
    return sum(x.min_cubes() for x in data)

print("Solution to part one:", part_one(data))
print("Solution to part two:", part_two(data))
