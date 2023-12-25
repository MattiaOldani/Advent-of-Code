# Solution: 3722

from collections import deque


def bfs(grid: list[list[str]], i: int, j: int) -> int:
    total = set()

    visited = set([(i,j)])
    
    check = deque([(i,j,64)])
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

print(bfs(grid, si, sj))
