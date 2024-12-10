# Solution: 1432


def search_trailheads(grid: list[list[int]], i: int, j: int, found: list[int]):
    if grid[i][j] == 9:
        return 1

    count = 0
    if i > 0 and grid[i - 1][j] == grid[i][j] + 1:
        count += search_trailheads(grid, i - 1, j, found)
    if i < len(grid) - 1 and grid[i + 1][j] == grid[i][j] + 1:
        count += search_trailheads(grid, i + 1, j, found)
    if j > 0 and grid[i][j - 1] == grid[i][j] + 1:
        count += search_trailheads(grid, i, j - 1, found)
    if j < len(grid[0]) - 1 and grid[i][j + 1] == grid[i][j] + 1:
        count += search_trailheads(grid, i, j + 1, found)

    return count


with open("input.txt", "r") as f:
    grid = [list(map(int, x.strip())) for x in f.readlines()]


count = 0
for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if cell == 0:
            count += search_trailheads(grid, i, j, 0)

print(count)
