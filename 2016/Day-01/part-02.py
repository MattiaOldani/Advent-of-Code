# Solution: 141

with open("input.txt", "r") as f:
    commands = f.readline().split(", ")

DIRECTIONS = [[0,1], [1,0], [0,-1], [-1,0]]
x,y,face = 0,0,0

visited = list([0,0])
for cmd in commands:
    face = (face + (1 if cmd[0] == "R" else -1) + 4) % 4
    move = DIRECTIONS[face]
    found = False
    for i in range(int(cmd[1:])):
        x += move[0]
        y += move[1]
        if (x,y) in visited:
            found = True
            break
        visited.append((x,y))
    if found:
        break

print(abs(x) + abs(y))
