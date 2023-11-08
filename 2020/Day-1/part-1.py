s = open("inputs.txt", "r").read()[:-1].split("\n")

a = [int(i) for i in s]

for x in a:
    if 2020-x in a:
        print((2020-x)*x)
        break
