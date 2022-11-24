# Solution: 239

with open("input.txt", "r") as f:
    commands = f.readline().split(", ")

DIRECTIONS = [[0,1], [1,0], [0,-1], [-1,0]]
x,y,face = 0,0,0

for cmd in commands:
    face = (face + (1 if cmd[0] == "R" else -1) + 4) % 4
    move = DIRECTIONS[face]
    x += (move[0] * int(cmd[1:]))
    y += (move[1] * int(cmd[1:]))

print(abs(x) + abs(y))
