import numpy as np
txt = open("input.txt", "r")
lines = txt.readlines()
txt.close()

nums = [[int(num) for num in list(rows) if num!="\n"] for rows in lines]

dim_y = len(nums)
dim_x = len(nums[0])

def sinks(l):
    bools = []
    for i in range(0,len(l)):
        if i==0: # first elem
            if l[0]<l[1]: # Right element is larger
                bools.append(True) # is Sink
            else:
                bools.append(False)
        elif i==len(l)-1: # last elem
            if l[-1]<l[-2]: # left element is larger
                bools.append(True) # is Sink
            else:
                bools.append(False)
        else:
            bools.append(l[i]<l[i+1] and l[i]<l[i-1])
    return bools


normal = [sinks(rows) for rows in nums]
trans = np.transpose([sinks(rows) for rows in np.transpose(nums)])


overlap = [[trans[i][j]and normal[i][j] for j in range(dim_x)] for i in range(dim_y)]

risk_lvl = [[nums[i][j] +1 for j in range(dim_x)if overlap[i][j] ] for i in range(dim_y)]



print(sum([sum(rows) for rows in risk_lvl]))

