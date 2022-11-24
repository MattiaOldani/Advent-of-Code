# Solution: 12578

with open("input.txt", "r") as f:
    commands = f.readlines()

DIRECTIONS = {
    "U" : [-1,0],
    "D" : [1,0],
    "L" : [0,-1],
    "R" : [0,1]
}

x,y = 1,1

for cmd in commands:
    for movement in cmd.strip():
        move = DIRECTIONS[movement]
        x += move[0]
        y += move[1]
        if not (0 <= x <= 2) or not (0 <= y <= 2):
            x -= move[0]
            y -= move[1]
    
    print(3*x + y + 1, end="")
