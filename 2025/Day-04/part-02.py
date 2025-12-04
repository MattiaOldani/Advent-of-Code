# Solution: 9784

with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]

rolls = set()
for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if cell == "@":
            rolls.add((i, j))

MOVES = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

count = 0
while True:
    to_remove = set()
    for i, j in rolls:
        current = 0
        for di, dj in MOVES:
            ni, nj = i + di, j + dj
            in_bounds = (0 <= ni < len(grid)) and (0 <= nj < len(line))
            if in_bounds and (ni, nj) in rolls:
                current += 1

        if current < 4:
            to_remove.add((i, j))

    if len(to_remove) == 0:
        break

    count += len(to_remove)
    rolls -= to_remove

print(count)
