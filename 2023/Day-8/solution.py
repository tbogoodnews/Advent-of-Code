import functools
import math

input_txt = open("input.txt")

data = input_txt.read()[:-1].split("\n")
moves = data[0]
nodes = {l.split(" ")[0] : {"L" : l[-9:-6], "R" : l[-4:-1] } for l in data[2:]}

@functools.cache
def move_step(current_node, direction):
    return nodes[current_node][direction]

def part_one():
    steps = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        direction = moves[steps % len(moves)]
        current_node = nodes[current_node][direction]
        steps += 1
    return steps

def part_two():
    factors = []
    a_nodes = [x for x in nodes.keys() if x[2] == "A"] # end in A
    z_nodes = [x for x in nodes.keys() if x[2] == "Z"]
    for n in a_nodes:
        steps = 0 
        current_node = n
        while current_node not in z_nodes:
            direction = moves[steps % len(moves)]
            current_node = nodes[current_node][direction]
            steps += 1
        factors.append(steps)
    return math.lcm(*factors)

print("Solution to part one:", part_one())
print("Solution to part two:", part_two())
