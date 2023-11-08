import numpy as np
file = "inputs.txt"
s = open(file, "r").read()[:-1].split("\n")


rx = 1
cycle = 0
instruction = s[0]
inst_i = 0
countdown = 1 if "noop" in instruction else 2

for i in range(0, 240):
    if i%40==0:
        print()

    if rx <= i%40 and rx+2 >= i%40:
        print("█", end="")
    else:
        print(" ", end="")

    if countdown == 0:
        inst_i += 1
        if "noop" not in instruction: # if times up on a non noop, add
            rx += int(instruction.split(" ")[1])
        instruction = s[inst_i] # advance
        if "noop" in instruction:
            countdown = 1
        else:
            countdown = 2
    countdown -= 1
        
print() 


