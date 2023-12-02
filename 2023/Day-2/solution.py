input_txt = open("input.txt")

class Game:
    def __init__(self, s):
        self.game_num = int(s.split(":")[0][5:])
        games = []
        for g in s.split(": ")[1].split("; "):
            d = {"red": 0, "green" : 0, "blue" : 0}
            for x in g.split(", "):
                d[x.split(" ")[1]] = int(x.split(" ")[0])
            games.append(d)
        self.games = games
            
    def possible(self):
        max_red = max(y["red"] for y in self.games)
        max_green = max(y["green"] for y in self.games)
        max_blue = max(y["blue"] for y in self.games)
        if max_red <= 12 and max_green <= 13 and max_blue <= 14:
            return True
        return False

    def min_cubes(self):
        max_red = max(y["red"] for y in self.games)
        max_green = max(y["green"] for y in self.games)
        max_blue = max(y["blue"] for y in self.games)
        return max_red * max_green * max_blue

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
