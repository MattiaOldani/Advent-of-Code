# Solution: 254

from collections import defaultdict


def in_bound(node, di, dj, R, C):
    return 0 <= node[0] + di < R and 0 <= node[1] + dj < C


with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]


positions = defaultdict(lambda: [])
for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if cell == ".":
            continue
        positions[cell] += [(i, j)]

R = len(grid)
C = len(grid[0])

antinode = set()
for nodes in positions.values():
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            a = nodes[i]
            b = nodes[j]

            di = a[0] - b[0]
            dj = a[1] - b[1]

            if in_bound(a, di, dj, R, C):
                antinode.add((a[0] + di, a[1] + dj))
            if in_bound(b, -di, -dj, R, C):
                antinode.add((b[0] - di, b[1] - dj))

print(len(antinode))
