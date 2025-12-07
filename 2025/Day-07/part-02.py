# Solution: 108924003331749

from collections import defaultdict


with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]

start = defaultdict(lambda: 0)
start[(0, grid[0].index("S"))] = 1

count = 0
for _ in range(len(grid) - 1):
    new_start = defaultdict(lambda: 0)
    for i, j in start:
        if grid[i + 1][j] == "^":
            new_start[(i + 1, j + 1)] += start[(i, j)]
            new_start[(i + 1, j - 1)] += start[(i, j)]
        else:
            new_start[(i + 1, j)] += start[(i, j)]

    start = new_start

print(sum(start.values()))
