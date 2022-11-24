# Solution: 516DD

with open("input.txt", "r") as f:
    commands = f.readlines()

DIRECTIONS = {
    "U" : [-1,0],
    "D" : [1,0],
    "L" : [0,-1],
    "R" : [0,1]
}

GRID = [
    [0,  0,   1,   0,  0],
    [0,  2,   3,   4,  0],
    [5,  6,   7,   8,  9],
    [0, "A", "B", "C", 0],
    [0,  0,  "D",  0,  0]
]

x,y = 2,0

for cmd in commands:
    for movement in cmd.strip():
        move = DIRECTIONS[movement]
        x += move[0]
        y += move[1]
        if not (0 <= x <= 4) or not (0 <= y <= 4) or GRID[x][y] == 0:
            x -= move[0]
            y -= move[1]
    
    print(GRID[x][y], end="")
