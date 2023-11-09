file = "test.txt"
s = open(file, "r").read()[:-1].split("\n")

s = [[l.split(" ")[0], int(l.split(" ")[1]) ] for l in s]

directions = {"U" : [0,1], "D" : [0,-1], "L" : [-1, 0], "R" : [1, 0]}

class knot:
    def __init__(self, parent = None, child = None):
        self.pos = [0,0]
        self.path = ["0x0"]
        self.parent = parent
        self.child = child
    
    def update(self):
        head = self.parent.pos
        tail = self.pos
        if tail[0]!=head[0] and tail[1]!=head[1]: # If on diagonal
            if abs(tail[0]-head[0])>1: # If there is a dist of more than to on x
                self.pos[1] = head[1] # Set the y coord to be equal
                self.pos[0] = (tail[0]+head[0])//2
            elif abs(tail[1]-head[1])>1:
                self.pos[0] = head[0]
                self.pos[1] = (tail[1]+head[1])//2
            else: # If stable diagonal
                return
        else:
            if abs(tail[0]-head[0])>1:
                self.pos[0] = (tail[0]+head[0])//2
            elif abs(tail[1]-head[1])>1:
               self.pos[1] = (tail[1]+head[1])//2
        self.path.append(str(self.pos[0]) + "x"+str(self.pos[1]))
        if self.child is not None:
             self.child.update() # call if distance distorted too much
    def add_child(self):
        self.child = knot(parent = self)

    def add_n_children(self,n):
        if n == 0:
            return None
        self.add_child()
        self.child.add_n_children(n-1) # Recurse

head = knot()
head.add_n_children(5)

for l in s:
    d_s = directions[l[0]]
    for steps in range(l[1]):
        head.pos = [head.pos[0]+d_s[0], head.pos[1]+d_s[1]]
        head.path.append(str(head.pos[0]) + "x"+str(head.pos[1]))
        head.child.update() 

k = head

while k.child is not None:
    k = k.child

print(len(set(k.path)))
print(k.path)

