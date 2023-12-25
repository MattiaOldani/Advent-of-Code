# Solution: 614864614526014

from collections import deque


def bfs(grid: list[list[str]], i: int, j: int, steps: int) -> int:
    total = set()

    visited = set([(i,j)])
    
    check = deque([(i,j,steps)])
    while len(check) > 0:
        i,j,step = check.popleft()

        if step % 2 == 0:
            total.add((i,j))

        if step == 0:
            continue

        for ni,nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] == "." and (ni,nj) not in visited:
                check.append((ni,nj,step-1))
                visited.add((ni,nj))
    
    return len(total)


with open("input.txt", "r") as f:
    grid = list(map(lambda x : list(x.strip()), f.readlines()))

si,sj = 0,0
for i,line in enumerate(grid):
    if "S" in line:
        si,sj = i,line.index("S")
        line[sj] = "."
        break

steps = 26501365
size = len(grid)
repeated_squares = steps // size

even_squares = (repeated_squares - 1) ** 2
odd_squares = (repeated_squares) ** 2

even_points = bfs(grid, si, sj, size * 2 + 1)
odd_points = bfs(grid, si, sj, size * 2)

corner_points = bfs(grid, 0, sj, size-1) + \
                bfs(grid, size-1, sj, size-1) + \
                bfs(grid, si, 0, size-1) + \
                bfs(grid, si, size-1, size-1)

remove_points = bfs(grid, 0, 0, size // 2 - 1) + \
                bfs(grid, 0, size-1, size // 2 - 1) + \
                bfs(grid, size-1, 0, size // 2 - 1) + \
                bfs(grid, size-1, size-1, size // 2 - 1)

half_points = bfs(grid, 0, 0, 3*size // 2 - 1) + \
              bfs(grid, 0, size-1, 3*size // 2 - 1) + \
              bfs(grid, size-1, 0, 3*size // 2 - 1) + \
              bfs(grid, size-1, size-1, 3*size // 2 - 1)

print(even_squares*even_points + odd_squares*odd_points + corner_points + repeated_squares*remove_points + (repeated_squares-1)*half_points)
