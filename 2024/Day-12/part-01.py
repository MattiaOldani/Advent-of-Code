# Solution: 1489582


def bfs(grid: list[list[str]], i: int, j: int):
    visited = set([(i, j)])
    to_check = set([(i, j)])

    letter = grid[i][j]
    while len(to_check) > 0:
        i, j = to_check.pop()

        if i > 0 and (i - 1, j) not in visited and grid[i - 1][j] == letter:
            visited.add((i - 1, j))
            to_check.add((i - 1, j))

        if (
            j < len(grid[0]) - 1
            and (i, j + 1) not in visited
            and grid[i][j + 1] == letter
        ):
            visited.add((i, j + 1))
            to_check.add((i, j + 1))

        if i < len(grid) - 1 and (i + 1, j) not in visited and grid[i + 1][j] == letter:
            visited.add((i + 1, j))
            to_check.add((i + 1, j))

        if j > 0 and (i, j - 1) not in visited and grid[i][j - 1] == letter:
            visited.add((i, j - 1))
            to_check.add((i, j - 1))

    return visited


def perimeter(visited: set) -> int:
    count = 0

    for cell in visited:
        i, j = cell

        if (i - 1, j) not in visited:
            count += 1
        if (i, j + 1) not in visited:
            count += 1
        if (i + 1, j) not in visited:
            count += 1
        if (i, j - 1) not in visited:
            count += 1

    return count


with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]


to_visit = set([(i, j) for i in range(len(grid)) for j in range(len(grid[0]))])

count = 0
while len(to_visit) > 0:
    i, j = to_visit.pop()
    visited = bfs(grid, i, j)
    count += len(visited) * perimeter(visited)
    to_visit.difference_update(visited)

print(count)
