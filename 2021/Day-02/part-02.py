# Solution: 1857958050

with open("input.txt", "r") as f:
    moves = list(map(lambda x : x.strip().split(" "), f.readlines()))

DIRECTIONS = {
    "up" : [0,0,-1],
    "down" : [0,0,1]
}

x,y,aim = 0,0,0
for move in moves:
    d = move[0]
    step = int(move[1])
    try:
        direction = DIRECTIONS[d]
        aim += direction[2] * step
    except:
        x += step
        y += (step * aim)   

print(x*y)
