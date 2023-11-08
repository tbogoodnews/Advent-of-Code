txt_file = open("input.txt", "r") # Open file

danger = txt_file.readlines() # read to list

txt_file.close()


pair_str_int = lambda s : [int(x) for x in s.split(",")] # pair to list
clean_pairs = lambda s : [pair_str_int(x) for x in s.replace("\n", "").split(" -> ")] # row to list

danger = [clean_pairs(bounds) for bounds in danger] # cleans

#min_x = min([min(entry[0][0], entry[1][0]) for entry in danger])
min_x = 0
max_x =  max([max(entry[0][0], entry[1][0]) for entry in danger])

#min_y = min([min(entry[0][1], entry[1][1]) for entry in danger])
min_y = 0
max_y =  max([max(entry[0][1], entry[1][1]) for entry in danger])

map_danger = [[0]*(max_x+1) for x in range (0, max_y+1)] # can't be done withot list comprehension

is_line = lambda p :  p[0][0]==p[1][0] or p[0][1]==p[1][1]

def update_map(m, p): # updates map
    for x in range(min(p[0][0], p[1][0]), max(p[0][0], p[1][0])+1):
        for y in range(min(p[0][1], p[1][1]), max(p[0][1], p[1][1])+1):
            m[y][x] = m[y][x] +1
    return m


for p in danger:
    if is_line(p):
        map_danger = update_map(map_danger, p)

danger_spots = sum([sum([i>=2for i in row]) for row in map_danger])

print(danger_spots)
