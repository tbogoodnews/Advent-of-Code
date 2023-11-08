txt_file = open("input.txt", "r") # Open file

values = txt_file.readlines() # read to list

txt_file.close()

# values = [int(val) for val in values] # Parse ints

num_numbers = len(values)
num_bits = 12

counts = [sum([int(j[i]) for j in values]) for i in range (0, num_bits)]

counts = [i > num_numbers/2 for i in counts] # 


gamma =  sum([2**i for i in range(0, num_bits) if counts[::-1][i]]) 

epsilon =  sum([2**i for i in range(0, num_bits) if not counts[::-1][i]])

print(counts)
print("Gamma is: ", gamma)
print("Epsilon is: ", epsilon)

print("Product is ", gamma*epsilon)
