# Solution: 1551

with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]

MOVES = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

count = 0
for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if cell == "@":
            current = 0
            for di, dj in MOVES:
                ni, nj = i + di, j + dj
                if 0 <= ni < len(grid) and 0 <= nj < len(line) and grid[ni][nj] == "@":
                    current += 1

            count += int(current < 4)

print(count)
