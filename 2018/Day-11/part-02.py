# Solution: 231 65 14

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
start_size = 1
max_square = -5 * 300 * 300 - 1
for size in range(1,301):
    print(f"Provo con {size}")
    for y in range(301-size):
        for x in range(301-size):
            count = 0
            for i in range(y,y+size):
                count += sum(grid[i][x:x+size])
            if count > max_square:
                start_x = x
                start_y = y
                start_size = size
                max_square = count

print(start_x + 1, start_y + 1, start_size)
