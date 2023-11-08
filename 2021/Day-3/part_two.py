txt_file = open("input.txt", "r") # Open file

values = txt_file.readlines() # read to list

num_bits = len(values[0])-1

txt_file.close()


def most_common(read_out, negated=False):
    num_numbers = len(read_out)
    counts = [sum([int(j[i]) for j in read_out]) for i in range (0, num_bits)]
    counts = [i >= num_numbers/2 for i in counts] #
    counts = [i if not negated else not i for i in counts]
    counts = [1 if j else 0 for j in counts]
    return counts

def filter_out(read_out, perfect_bit, i):
    clean = []
    for j in read_out:
        if perfect_bit==int(str(j)[i]):
            clean.append(j)
    return clean 

ox_list = values
ox_compare_on = 0
while len(ox_list)>1:
    perfect_ox_bit = most_common(ox_list)[ox_compare_on]
    ox_list = filter_out(ox_list, perfect_ox_bit, ox_compare_on)
    ox_compare_on += 1

print(ox_list)

co_list = values
co_compare_on = 0
while len(co_list)>1:
    perfect_co_bit = most_common(co_list, True)[co_compare_on],
    co_list = filter_out(co_list, perfect_co_bit, co_compare_on)
    co_compare_on += 1

print(co_list)
