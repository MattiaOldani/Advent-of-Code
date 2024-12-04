# Solution: 1886

with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]


count = 0
for i, line in enumerate(grid):
    if i == 0 or i == len(grid) - 1:
        continue

    for j in range(1, len(line) - 1):
        fd = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
        sd = grid[i + 1][j - 1] + grid[i][j] + grid[i - 1][j + 1]

        if fd in ["MAS", "SAM"] and sd in ["MAS", "SAM"]:
            count += 1

print(count)
