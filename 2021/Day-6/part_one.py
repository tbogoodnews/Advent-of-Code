txt_file = open("input.txt", "r")
fish = [int(i) for i in txt_file.read().split(",")] # read in fish
txt_file.close() 
num_days = 80

for days in range(0,num_days):
    new_fish = []
    for i in range(0, len(fish)):
        if fish[i]==0: # Spawning
            new_fish.append(8) # adds on new fish
            fish[i]=6  # resets to 6
        else:
            fish[i] -= 1 # removes a day
    fish += new_fish # appends on new fish

print(len(fish))
