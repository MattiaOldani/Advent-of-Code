# Solution: 1693300

with open("input.txt", "r") as f:
    moves = list(map(lambda x : x.strip().split(" "), f.readlines()))

DIRECTIONS = {
    "forward" : [1,0],
    "up" : [0,-1],
    "down" : [0,1]
}

x,y = 0,0
for move in moves:
    d = move[0]
    step = int(move[1])
    direction = DIRECTIONS[d]
    x += direction[0] * step
    y += direction[1] * step

print(x*y)
