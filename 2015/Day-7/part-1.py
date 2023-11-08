import numpy as np
file = "inputs.txt"
s = open(file).read()[:-1].split("\n")

values = dict()


def fetch(register):
    if register.isnumeric(): # okay, so not really a register
        return np.uint16(register)
    if register not in values.keys():
        values[register] = np.uint16(0)
    return values[register]

for l in s:
    expression, output = l.split(" -> ")
    spaces = expression.count(" ")
    match spaces:
        case 0: # assignment op
            values[output] = fetch(expression)
        case 1: # not op
            register = fetch(expression.split(" ")[1])
            values[output] = ~register
        case 2:
            l, operator, r = expression.split(" ")
            l, r = fetch(l), fetch(r)
            match operator:
                case "LSHIFT":
                    values[output] = np.uint16(int(l)<< int(r))
                case "RSHIFT":
                    values[output] = np.uint16(int(l) >> int(r))
                case "AND":
                    values[output] = l & r
                case "OR":
                    values[output] = l | r

print(values)
print(values["a"])
