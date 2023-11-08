file = "inputs.txt"
s = open(file, "r").read()[:-1].split("\n")

class Folder:
    def __init__(   self,
                    name, 
                    parent = None):
        self.name = name
        self.parent = parent
        self.files = dict() # files are key value dict
        self.nested = []

    def total_nested(self):
        return self.total_dir() + sum([c.total_nested() for c in self.nested])

    def total_dir(self):
        return sum(list(self.files.values()))

    def find_child(self, name):
        for kid in self.nested:
            if kid.name == name:
                return kid
        return None
    
    def add_dir(self, name):
        self.nested.append(Folder(name = name, parent = self))

    def part_one(self):
        total = 0
        
        if self.total_nested() <= 100000:
            total += self.total_nested()


        for d in self.nested:
            total +=  d.part_one()
        return total 

    def nested_sizes(self):
        vals = [self.total_nested()]
        for f in self.nested:
            vals = vals + f.nested_sizes()
        return vals


root = Folder("/")
current = root

for line in s[1:]:
    if line[0] == "$": # if instruction
        if line == "$ cd ..":
            if current.name == "/":
                continue
            else:
                current = current.parent # CD up
        elif line == "$ ls":
            continue # Do nothing
        elif "cd" in line: # If `cd` to a folder
            mv_dir = line.split(" ")[-1]
            current = current.find_child(mv_dir)
    else: # Parse file
        info = line.split(" ")
        if info[0] == "dir":
            current.add_dir(info[1])
        else:
            current.files[info[1]] = int(info[0])


print("Part one:", root.part_one())