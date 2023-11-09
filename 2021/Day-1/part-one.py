txt_file = open("input.txt", "r") # open file

depths = txt_file.readlines() # Read to list

depths = [int(level) for level in depths] # parse as ints

print(sum([ depths[i] < depths[i+1] for i in range (0,len(depths)-1)])) # Print amount

txt_file.close()
