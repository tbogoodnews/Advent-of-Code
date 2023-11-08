import math
s = int(open("inputs.txt", "r").read()[:-1])

dist  = math.ceil(math.sqrt(s)) // 2 * 2 + 1# ring
r_corner = dist**2
ring = (dist-1)//2

# 37  36  35  34  33  32  31
# 38  17  16  15  14  13  30
# 39  18   5   4   3  12  29
# 40  19   6   1   2  11  28
# 41  20   7   8   9  10  27
# 42  21  22  23  24  25  26
# 43  44  45  46  47  48  49

# 1, 9, 25, 49
# 1, 3, 5, 7
# 0, 1, 2, 3

prev_r_corner = ((dist-2)**2)

# side is 1 for east or top right, 2 for north or top left, 3 for west...
side = math.ceil((s-prev_r_corner)/((r_corner-prev_r_corner)/4))

print(dist, prev_r_corner, r_corner, ring)
print(side)

closest_corner = prev_r_corner + (side*(dist-1))

dist_corner = closest_corner - s

offset = abs(((dist-1)/2)-dist_corner)

print("trek", ring, "and", offset)

print("Manhattan distance:", ring+offset)


