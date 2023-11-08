s = [int(i) for i in open("inputs.txt", "r").read()[:-1].split("\n")]

def f(x): 
    y = (x//3)-2
    if y> 5:
        return y + f(y)
    else:
        return y

print(sum([f(x) for x in s]))



