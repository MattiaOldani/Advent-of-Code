# Solution: 371

with open("input.txt", "r") as f:
    end = int(f.readline().strip())

x,y,direction = 0,0,0

FACE = [[1,0], [0,1], [-1,0], [0,-1]]

step = 1
counter = 0
walked = 1

while walked < end:
    direction = (direction + 1) % 4
    move = FACE[direction]

    i = 0
    while i < step and walked < end:
        x += move[0]
        y += move[1]
        walked += 1
        i += 1

    counter += 1

    if counter == 2:
        step += 1
        counter = 0

print(abs(x) + abs(y))
