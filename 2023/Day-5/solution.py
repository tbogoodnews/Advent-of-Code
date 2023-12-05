input_txt = open("input.txt")

data = input_txt.read()[:-1].split("\n\n")

def traverse(value, depth = 1):
    if depth >= len(data):
        return value
    level = data[depth].split("\n")[1:]
    for v in level:
        dest_range_start = int(v.split()[0])
        source_range_start = int(v.split()[1])
        range_len = int(v.split()[2])
        if value >= source_range_start and value < source_range_start + range_len:
            return traverse(dest_range_start + (value - source_range_start), depth + 1)
    return traverse(value, depth + 1)


def part_one(s):
    seeds = [int(x) for x in s[0].split()[1:]]
    return min(traverse(y) for y in seeds)
    #for seeds

def return_ranges(start, s_range, depth):
    # Only need to return destination and ranges, then recurse
    level = data[depth].split("\n")[1:]
    for v in level:
        dest_range_start = int(v.split()[0])
        source_range_start = int(v.split()[1])
        range_len = int(v.split()[2])
        if start >= source_range_start and start < source_range_start + range_len: # 
            destination = dest_range_start + (start - source_range_start)
            avalible_range = (dest_range_start + range_len) - destination # How much useable range
            if s_range <= avalible_range: # If the range is less than remaining range, then no more recursion
                return [[destination, s_range]]
            else:
                return [[destination, avalible_range]] + return_ranges(start + avalible_range, s_range - avalible_range, depth)
    # Else, return identity mapping for elements up to next closest
    sources = sorted([int(v.split()[1]) for v in level]) # Sorted list of sources
    if start > max(sources): # If exceeding all sources (and not within range), identity all
        return [[start, s_range]]
    barley_larger = sources[[v > start for v in sources].index(True)] # Find first that's larger
    if barley_larger-start >= s_range: # If distance to next is greater than remaining range, end recurse
        return [[start, s_range ]]
    return [[start, barley_larger-start ]] + return_ranges(barley_larger, s_range - (barley_larger-start), depth) 

def part_two(s):
    mappings = [int(x) for x in s[0].split()[1:]]
    mappings = [[mappings[2*p], mappings[(2*p)+1]] for p in range(len(mappings)//2)]
    for d in range(1, len(data)):
        temp = []
        for m in mappings:
            temp += return_ranges(m[0], m[1], d)
        mappings = temp
    return min(c[0] for c in mappings) 


print("Solution to part one:", part_one(data))
print("Solution to part two:", part_two(data))
