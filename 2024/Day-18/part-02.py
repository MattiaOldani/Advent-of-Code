# Solution: 44,64

import heapq
from collections import defaultdict


with open("input.txt", "r") as f:
    cells = [list(map(int, x.split(","))) for x in f.readlines()]


SIZE = 71
grid = [["." for _ in range(SIZE)] for _ in range(SIZE)]
for x, y in cells[:1024]:
    grid[y][x] = "#"

for x, y in cells[1024:]:
    grid[y][x] = "#"

    distance = defaultdict(lambda: float("inf"))
    distance[(0, 0)] = 0

    queue = [(0, 0, 0)]

    while queue:
        steps, cy, cx = heapq.heappop(queue)
        if steps > distance[(cy, cx)]:
            continue

        for sy, sx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny = cy + sy
            nx = cx + sx
            if 0 <= ny < SIZE and 0 <= nx < SIZE and grid[ny][nx] == ".":
                if distance[(cy, cx)] + 1 < distance[(ny, nx)]:
                    distance[(ny, nx)] = distance[(cy, cx)] + 1
                    heapq.heappush(queue, (distance[(cy, cx)] + 1, ny, nx))

    if distance[(SIZE - 1, SIZE - 1)] == float("inf"):
        print(f"{x},{y}")
        break
