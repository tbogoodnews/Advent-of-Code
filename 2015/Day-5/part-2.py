s = open("inputs.txt", "r").read()[:-1]

l = s.split("\n")

def double_pair(s):
    for i in range(len(s)-1):
        search = s[i:i+2]
        split = s[:i] + " "+ s[i+2:]
        if search in split:
            return True
    return False

def skip_check(s):
    for i in range(len(s)-2):
        if s[i]==s[i+2]:
            return True
    return False

matches = []

for i in l:
    if double_pair(i) and skip_check(i):
        matches.append(i)


print(len(matches))

