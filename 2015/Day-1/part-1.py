s = open("inputs.txt", "r").read()

open_p = s.count("(")
close_p = s.count(")")
print(open_p - close_p)


