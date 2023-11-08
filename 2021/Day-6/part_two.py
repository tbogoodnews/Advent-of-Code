txt_file = open("input.txt", "r") # read input
fish = [int(i) for i in txt_file.read().split(",")] # parse input
txt_file.close()

num_days = 256
spawn_timer = [0]*9 # blank index from 0 to 8

for i in fish: # moves next fish to spawn timer
    spawn_timer[i] += 1

for days in range(0,num_days): # iterates through days
    num_spawning = spawn_timer[0] # holder variable, could be improved
    for i in range(0, len(spawn_timer)-1): # iterates through new days
        spawn_timer[i] = spawn_timer[i+1] # Moves day forward
    spawn_timer[6] += num_spawning # adds fish that are going to spawn again
    spawn_timer[8] = num_spawning # Adds new fish

print(sum(spawn_timer))
