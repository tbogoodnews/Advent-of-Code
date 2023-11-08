file = "inputs.txt"
s = open(file, "r").read()[:-1].split("\n")

a = [int(i) for i in s]


def search_prods(val, l):
    for x in l:
        if val-x in l:
            return x*(val-x)
    return None

for y in range(len(a)):
    search = search_prods(2020-a[y], a[:y] + a[1+y:])
    if search is not None:
        print(search*a[y])
        break

