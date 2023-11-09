txt_file = open("input.txt", "r") # Open file

depths = txt_file.readlines() # read to list

depths = [int(level) for level in depths] # Parse ints

print(sum([sum(depths[i:i+3]) < sum(depths[i+1:i+4]) for i in range (0,len(depths)-3)])) # list comprehension nasty

txt_file.close()
