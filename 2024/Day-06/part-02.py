# Solution: 1443


def search(grid, x, y):
    facing = "^"
    visited = set()

    out = False
    while True:
        if (x, y, facing) in visited:
            break

        visited.add((x, y, facing))

        match facing:
            case "^":
                if y > 0:
                    if grid[y - 1][x] == ".":
                        y -= 1
                    else:
                        facing = ">"
                else:
                    out = True
            case ">":
                if x < len(grid[0]) - 1:
                    if grid[y][x + 1] == ".":
                        x += 1
                    else:
                        facing = "v"
                else:
                    out = True
            case "v":
                if y < len(grid) - 1:
                    if grid[y + 1][x] == ".":
                        y += 1
                    else:
                        facing = "<"
                else:
                    out = True
            case "<":
                if x > 0:
                    if grid[y][x - 1] == ".":
                        x -= 1
                    else:
                        facing = "^"
                else:
                    out = True

        if out:
            break

    return (set([(x, y) for x, y, _ in visited]), not out)


with open("input.txt", "r") as f:
    start_grid = [list(x.strip()) for x in f.readlines()]


start_x, start_y = 0, 0
for i, line in enumerate(start_grid):
    for j, el in enumerate(line):
        if el == "^":
            start_x, start_y = j, i
            start_grid[i][j] = "."
            break

count = 0
route, _ = search(start_grid, start_x, start_y)
route.remove((start_x, start_y))

for x, y in route:
    grid = [[el for el in line] for line in start_grid]
    grid[y][x] = "#"

    _, loop = search(grid, start_x, start_y)

    if loop:
        count += 1

print(count)
