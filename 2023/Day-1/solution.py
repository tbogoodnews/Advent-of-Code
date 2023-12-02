import re
input_txt = open("input.txt")

data = input_txt.read()[:-1]
data = data.split("\n")

def part_one(s):
    l = ["".join(re.findall(r'\d+', j)) for j in s] 
    l = [int(k[0]+k[-1]) for k in l]
    return sum(l)

replace = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}

def process_str(s):
    l = []
    for d in range(len(s)):
        if s[d].isdigit():
            l.append(s[d])
        else:
            for x in range(d,len(s)+1):
                if s[d:x] in replace.keys():
                    l.append(str(replace[s[d:x]]))
                    break
    return l


def part_two(s):
    l = [process_str(x) for x in s]
    l = [int(str(y[0]) + str(y[-1])) for y in l]
    return sum(l)

print("Solution to part one:", part_one(data))
print("Solution to part two:", part_two(data))
