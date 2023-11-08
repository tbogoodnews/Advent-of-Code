input_txt = open("input.txt")

data = input_txt.read()
  
data = data.split("\n\n")

data = [sum([int(j) for j in i.split("\n") if j!=""]) for i in data]

print(max(data))
