# Solution: 35401

with open("input.txt", "r") as f:
    moves = list(map(lambda x : x.strip().split(), f.readlines()))

DIRECTIONS = {"R": (1,0), "D": (0,-1), "L": (-1,0), "U": (0,1)}

vertex = []

x,y  = 0,0
perimeter = 0
for move in moves:
    direction, count, _ = move
    move = DIRECTIONS[direction]
    
    x = x + int(count)*move[0]
    y = y + int(count)*move[1]

    vertex.append((x,y))
    perimeter += int(count)

vertex.insert(0, vertex.pop())

area = 0
for i in range(len(vertex)):
    _,cy = vertex[i]
    nx,_ = vertex[(i+1)%len(vertex)]
    px,_ = vertex[i-1]
    area += cy * (px - nx)

print((abs(area) + perimeter) // 2 + 1)
