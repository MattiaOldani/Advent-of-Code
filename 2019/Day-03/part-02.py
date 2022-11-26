# Solution: 3454

with open("input.txt", "r") as f:
    paths = f.readlines()

MOVE = {
    "U" : [0,1],
    "D" : [0,-1],
    "R" : [1,0],
    "L" : [-1,0]
}

delay = 0
visited = dict()
collision = dict()
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
                dummy = visited[(x,y)]
                collision[(x,y)] = 0
            except:
                visited[(x,y)] = 0

try:
    del collision[(0,0)]
except:
    pass

steps = list()
for i in range(len(paths)):
    path = paths[i]
    x,y = 0,0
    counter = 0
    path = list(map(lambda x : [x[0], int(x[1:])], path.strip().split(",")))
    
    sus = dict()
    for move in path:
        direction = MOVE[move[0]]
        step = move[1]
        for i in range(step):
            x += direction[0]
            y += direction[1]
            counter += 1

            if (x,y) in collision.keys():
                if (x,y) not in sus.keys():
                    sus[(x,y)] = counter
    
    steps.append(sus)

delay = 0
collisions = list(sus.keys())
for c in collisions:
    try:
        c1 = steps[0][c]
        c2 = steps[1][c]
    except:
        continue
    if delay == 0 or (c1+c2) < delay:
        delay = c1 + c2

print(delay)
