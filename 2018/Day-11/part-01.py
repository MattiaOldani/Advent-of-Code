# Solution: 20 46

with open("input.txt", "r") as f:
    serial = int(f.read().strip())

grid = [[0 for _ in range(300)] for _ in range(300)]

for y,line in enumerate(grid):
    for x in range(len(line)):
        rack = x + 11
        yc = y + 1
        grid[y][x] = ((rack * yc + serial) * rack // 100) % 10 - 5

start_x = 0
start_y = 0
max_square = -46
for y in range(297):
    for x in range(297):
        count = 0
        for i in range(y,y+3):
            count += sum(grid[i][x:x+3])
        if count > max_square:
            start_x = x
            start_y = y
            max_square = count

print(start_x + 1, start_y + 1)
