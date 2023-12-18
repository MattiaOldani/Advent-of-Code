# Solution: 48020869073824

with open("input.txt", "r") as f:
    codes = list(map(lambda x : x.strip().split()[2], f.readlines()))

DIRECTIONS = {"R": (1,0), "D": (0,-1), "L": (-1,0), "U": (0,1)}
N_TO_DIRECTION = {"0": "R", "1": "D", "2": "L", "3": "U"}

vertex = []

x,y  = 0,0
perimeter = 0
for rgb in codes:
    move = DIRECTIONS[N_TO_DIRECTION[rgb[-1]]]
    count = int(rgb[:5], 16)
    
    x = x + count*move[0]
    y = y + count*move[1]

    vertex.append((x,y))
    perimeter += count

vertex.insert(0, vertex.pop())

area = 0
for i in range(len(vertex)):
    _,cy = vertex[i]
    nx,_ = vertex[(i+1)%len(vertex)]
    px,_ = vertex[i-1]
    area += cy * (px - nx)

print((abs(area) + perimeter) // 2 + 1)
