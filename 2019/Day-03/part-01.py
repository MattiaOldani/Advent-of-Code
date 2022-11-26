# Solution: 217

with open("input.txt", "r") as f:
    paths = f.readlines()

MOVE = {
    "U" : [0,1],
    "D" : [0,-1],
    "R" : [1,0],
    "L" : [-1,0]
}

visited = dict()
collision = list()

for path in paths:
    x,y = 0,0
    path = list(map(lambda x : [x[0], int(x[1:])], path.strip().split(",")))
    
    for move in path:
        direction = MOVE[move[0]]
        step = move[1]
        for i in range(step):
            x += direction[0]
            y += direction[1]

            try:
                sus = visited[(x,y)]
                collision.append((x,y))
            except:
                visited[(x,y)] = 0

while collision.count([0,0]) > 0:
    collision.remove([0,0])

collision = list(map(lambda x : abs(x[0]) + abs(x[1]), collision))

print(min(collision))
