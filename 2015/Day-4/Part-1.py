import hashlib

s = open("inputs.txt", "r").read()[:-1]



for i in range(10000000):
    hashed = hashlib.md5((s + str(i)).encode()).hexdigest()
    if hashed[:5]=="00000":
        print(hashed)
        print(i)
        break
