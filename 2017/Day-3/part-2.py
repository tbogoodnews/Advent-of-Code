import math
s = int(open("inputs.txt", "r").read()[:-1])

pos = dict()

x = 0
y = 0

pos[0] = {"x": 0, "y" : 0, "val": 1}
dir = "n"

for i in range (1, 10):
    # add 2 if corner, 3 if non corner. Use loop around for search back
    pass
