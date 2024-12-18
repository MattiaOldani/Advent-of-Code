# Solution: 232

import heapq
from collections import defaultdict


with open("input.txt", "r") as f:
    cells = [list(map(int, x.split(","))) for x in f.readlines()[:1024]]


SIZE = 71
grid = [["." for _ in range(SIZE)] for _ in range(SIZE)]
for x, y in cells:
    grid[y][x] = "#"

distance = defaultdict(lambda: float("inf"))
distance[(0, 0)] = 0

queue = [(0, 0, 0)]

while queue:
    steps, y, x = heapq.heappop(queue)
    if steps > distance[(y, x)]:
        continue

    for sy, sx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny = y + sy
        nx = x + sx
        if 0 <= ny < SIZE and 0 <= nx < SIZE and grid[ny][nx] == ".":
            if distance[(y, x)] + 1 < distance[(ny, nx)]:
                distance[(ny, nx)] = distance[(y, x)] + 1
                heapq.heappush(queue, (distance[(y, x)] + 1, ny, nx))

print(distance[(SIZE - 1, SIZE - 1)])
