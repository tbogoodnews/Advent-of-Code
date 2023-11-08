txt_file = open("input.txt", "r") # read input

display = txt_file.readlines()
txt_file.close()


unique = lambda s : len(s) in [2,3,4,7]
right = [c.split(" | ")[1] for c in display]
right = [c.replace("\n", "").split(" ") for c in right]



right = sum([sum(map(unique, l)) for l in right])

print(right)
