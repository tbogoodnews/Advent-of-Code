input_txt = open("input.txt")

data = input_txt.read()
  
# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data = data.split("\n\n")

data = [sum([int(j) for j in i.split("\n") if j!=""]) for i in data]

print(sum(sorted(data)[-3:]))
