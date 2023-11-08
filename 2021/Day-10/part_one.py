txt_file = open("example.txt", "r") # Open file
nav = txt_file.readlines() # read to list
txt_file.close()

bracs = {"{":"}", "(":")", "[":"]", "<":">"} # dict obj of brackets

points = {")": 3, "]": 57, "}":1197, ">": 25137} # Dict object of points

###

nav = [row.replace("\n", "") for row in nav]


is_incomplete = lambda row : 0!= sum([-1 if val in list(bracs.keys()) else 1 for val in row])

incomplete = [row for row in nav if is_incomplete(row)]

corrupted = [line for line in nav if line not in incomplete] # gives the complement of nav and incomplete

###



print(corrupted)

