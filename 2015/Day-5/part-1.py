import re


s = open("inputs.txt", "r").read()[:-1]

l = s.split("\n")


def check(s):
    if ("ab" in s) or ("cd" in s) or ("pq" in s) or ("xy" in s):
        return False
    if len(re.findall("[aeiou]", s)) < 3:
        return False
    if True in [s[i]==s[i+1]for i in range(len(s)-1)]:
        return True

matches = []

for i in l:
    if check(i):
        matches.append(i)

print(len(matches))

