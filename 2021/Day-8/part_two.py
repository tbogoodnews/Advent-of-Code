txt_file = open("input.txt", "r") # read input

display = txt_file.readlines()
txt_file.close()

unique_vals = [2,3,4,7]
 
unique = lambda s : len(s) in unique_vals 

all_vals = [c.replace(" | ", " ") for c in display]
all_vals = [c.replace("\n", "").split(" ") for c in all_vals]

easy_digits = lambda v : [1, 7, 4, 8][unique_vals.index(len(v))] 

str_in_str = lambda s, t : len(s) == sum([char in t for char in s])


def len_six(i, c, v):
    one_code = c[v.index(1)] 
    if str_in_str(one_code, i):# if right side full, ie overlap with 1
        four_code = c[v.index(4)]
        if str_in_str(four_code, i):
            return 9
        else:
            return 0
    else:
        return 6 



def remaining(i, c, v):
    one_code = c[v.index(1)] 
    if not str_in_str(one_code, i):# if right side not full, ie overlap with 1
        six_code = c[v.index(6)]
        if one_code[0] in six_code: 
            top_right = one_code[0]
        else:
            top_right = one_code[1]
        if top_right in i:
            return 5
        else:
            return 2
    else:
        return 3 


def fill(l):
    c = list(set(l))  
    vals = [easy_digits(i) if unique(i) else -1 for i in c] # values for unique digit lens
    vals = [len_six(c[i], c, vals) if len(c[i])==6 else vals[i] for i in range(0,len(c))] # classify 0, 6, 9
    vals = [remaining(c[i], c, vals) if vals[i]==-1 else vals[i] for i in range(0,len(c))] # classify 2, 3, 5
    return [vals[c.index(j)] for j in l]


values = [fill(rows) for rows in all_vals] # gets the digits

row_to_num = lambda l : 1000*l[-4]+100*l[-3]+10*l[-2]+l[-1]

values = [row_to_num(rows) for rows in values] 




print(sum(values))
