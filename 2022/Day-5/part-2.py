import re

file = "inputs.txt"
order, moves = open(file, "r").read()[:-1].split("\n\n") # Split into start and moves
order = order.split("\n") # break lines into list

moves = [re.split("move | from | to ", i) for i in moves.split("\n") ] # remove words
moves = [[int(j[1]), int(j[2]), int(j[3])] for j in moves] # cast to int and extract

n_s = int(order[-1].rsplit(" ", 2)[-2]) # num stacks
stacks = dict(zip( range(1,n_s+1), [[] for i in range(n_s)])) # Make crate stacks, first values are top

for l in order:
    for x in range(n_s):
        letter = l[(4*x)+1]
        if letter !=" ": # if not empty
            stacks[x+1].append(letter)

for k in moves: # move the stacks
    grab = stacks[k[1]][:k[0]] # mov
    # grab = grab[::-1] # flip
    stacks[k[1]] = stacks[k[1]][k[0]:] # move off
    stacks[k[2]] = grab + stacks[k[2]] # add to new stack 

# Join word
print("Answer:", "".join([stacks[d][0] for d in range(1,n_s+1)]) )

