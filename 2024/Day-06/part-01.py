# Solution: 4696

with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]


x, y = 0, 0
for i, line in enumerate(grid):
    for j, el in enumerate(line):
        if el == "^":
            x, y = j, i
            grid[i][j] = "."
            break

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

print(len(set([(x, y) for x, y, _ in visited])))
