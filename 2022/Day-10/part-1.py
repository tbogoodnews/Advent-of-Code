file = "inputs.txt"
s = open(file, "r").read()[:-1].split("\n")


rx = 1
checkpoints = [20, 60, 100, 140, 180, 220]
check_i = 0 # index for above
total = 0
inst_i = 0
instruction = s[inst_i]
countdown = 1 if "noop" in instruction else 2

for i in range(0, checkpoints[-1]+1):
    if i == checkpoints[check_i]:
        total += checkpoints[check_i] * rx
        check_i += 1
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
        

print(total)

