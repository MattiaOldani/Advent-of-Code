# Solution: 1651

with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]

start = set([(0, grid[0].index("S"))])

count = 0
for _ in range(len(grid) - 1):
    new_start = set()
    for i, j in start:
        if grid[i + 1][j] == "^":
            new_start.add((i + 1, j + 1))
            new_start.add((i + 1, j - 1))
            count += 1
        else:
            new_start.add((i + 1, j))
    start = new_start

print(count)
