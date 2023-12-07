import numpy as np
import math
input_txt = open("input.txt")

data = input_txt.read()[:-1].split("\n")
data = [d.split()[1:] for d in data]

lower = lambda time, distance : ((time**2 - (4*distance))**0.5 - time) / (-2)
upper = lambda time, distance : (-1 * (time**2 - (4*distance))**0.5 - time) / (-2)
beaten = lambda time, distance : math.floor(upper(time, distance)) - math.ceil(lower(time, distance)) +1

def part_one(s):
    s = [[int(s[0][x]), int(s[1][x])] for x in range(len(data[0]))]
    return np.prod([1] + [beaten(x[0], x[1]) for x in s])

def part_two(s):
    time = int("".join(s[0]))
    distance = int("".join(s[1]))
    return beaten(time, distance)
 
print("Solution to part one:", part_one(data))
print("Solution to part two:", part_two(data))
