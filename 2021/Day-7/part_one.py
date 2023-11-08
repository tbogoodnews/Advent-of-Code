txt_file = open("input.txt", "r") # read input
crabs = [int(i) for i in txt_file.read().split(",")] # parse input

max_crab = max(crabs)
min_crab = 0

fuel_costs = [sum([abs(center-crab) for crab in crabs]) for center in range (0,max_crab)]


print("Position: ", fuel_costs.index(min(fuel_costs)))
print("Fuel used: ", min(fuel_costs))
