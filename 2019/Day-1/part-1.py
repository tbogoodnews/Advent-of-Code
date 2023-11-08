s = [int(i) for i in open("inputs.txt", "r").read()[:-1].split("\n")]

print(sum([(x//3)-2 for x in s]))



