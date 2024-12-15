# Solution: 1509780


def bfs(grid, i, j, i_step, reverse):
    to_check = set([(i, j), (i, j + 1)])
    visited = set([(i, j), (i, j + 1)])

    while len(to_check) > 0:
        i, j = to_check.pop()
        if grid[i + i_step][j] == "[":
            to_check.add((i + i_step, j))
            to_check.add((i + i_step, j + 1))
            visited.add((i + i_step, j))
            visited.add((i + i_step, j + 1))
        elif grid[i + i_step][j] == "]":
            to_check.add((i + i_step, j))
            to_check.add((i + i_step, j - 1))
            visited.add((i + i_step, j))
            visited.add((i + i_step, j - 1))

    return sorted(list(visited), key=lambda x: x[0], reverse=reverse)


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")


grid = [
    list(x.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@."))
    for x in data[0].split("\n")
]
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
        case "^" | "v":
            i_step = -1 if move == "^" else 1
            reverse = False if move == "^" else True
            if grid[i + i_step][j] == ".":
                i = i + i_step
            elif grid[i + i_step][j] in ["[", "]"]:
                visited = bfs(
                    grid,
                    i + i_step,
                    j - 1 if grid[i + i_step][j] == "]" else j,
                    i_step,
                    reverse,
                )

                to_move = True
                for ii, jj in visited:
                    if grid[ii + i_step][jj] == "#":
                        to_move = False
                        break

                if to_move:
                    for ii, jj in visited:
                        grid[ii + i_step][jj] = grid[ii][jj]
                        grid[ii][jj] = "."
                    i = i + i_step
        case "<" | ">":
            j_step = -1 if move == "<" else 1
            starter = "]" if move == "<" else "["
            if grid[i][j + j_step] == ".":
                j = j + j_step
            elif grid[i][j + j_step] == starter:
                sj = j + j_step
                while grid[i][sj] in ["[", "]"]:
                    sj += j_step
                if grid[i][sj] == ".":
                    for t in range(sj, j, -j_step):
                        grid[i][t] = grid[i][t - j_step]
                    j = j + j_step

count = 0
for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if cell == "[":
            count += 100 * i + j

print(count)
