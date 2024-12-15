# Solution: 1479679

with open("input.txt", "r") as f:
    data = f.read().split("\n\n")


grid = [list(x) for x in data[0].split("\n")]
moves = "".join(data[1].split("\n"))

i, j = 0, 0
for ii, line in enumerate(grid):
    for jj, cell in enumerate(line):
        if cell == "@":
            i, j = ii, jj
            grid[i][j] = "."
            break

for move in moves:
    match move:
        case "^":
            i_step, j_step = -1, 0
        case ">":
            i_step, j_step = 0, 1
        case "v":
            i_step, j_step = 1, 0
        case "<":
            i_step, j_step = 0, -1

    if grid[i + i_step][j + j_step] == ".":
        i = i + i_step
        j = j + j_step
    elif grid[i + i_step][j + j_step] == "O":
        si = i + i_step
        sj = j + j_step
        while grid[si][sj] == "O":
            si += i_step
            sj += j_step
        if grid[si][sj] == ".":
            grid[si][sj] = "O"
            grid[i + i_step][j + j_step] = "."
            i = i + i_step
            j = j + j_step

count = 0
for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if cell == "O":
            count += 100 * i + j

print(count)
