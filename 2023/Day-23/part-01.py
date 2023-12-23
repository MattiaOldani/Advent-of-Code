# Solution: 2106

def dfs(edges: dict, start: tuple) -> int:
    if start == end:
        return 0

    count = []
    for ei,ej,steps in edges[start]:
        count.append(steps + dfs(edges, (ei,ej)))

    return max(count)


with open("input.txt", "r") as f:
    grid = list(map(lambda x : list(x.strip()), f.readlines()))

start = (0, grid[0].index("."))
end = (len(grid)-1, grid[-1].index("."))

vertex = [start, end]
for i,line in enumerate(grid):
    for j,element in enumerate(line):
        if element == "#":
            continue

        count = 0
        for ni,nj in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and not grid[ni][nj] == "#":
                count += 1
        
        if count >= 3:
            vertex.append((i,j))

edges = dict([(v,[]) for v in vertex])

DIRECTIONS = {
    ">": [(0,1)],
    "v": [(1,0)],
    "<": [(0,-1)],
    "^": [(-1,0)],
    ".": [(0,1), (1,0), (0,-1), (-1,0)]
}

for si,sj in vertex:
    visited = set([(si,sj)])

    start_positions = [(si,sj,0)]
    while len(start_positions) > 0:
        i,j,step = start_positions.pop()

        if step > 0 and (i,j) in vertex:
            edges[(si,sj)].append((i,j,step))
            continue

        for ci,cj in DIRECTIONS[grid[i][j]]:
            ni = i + ci
            nj = j + cj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and not grid[ni][nj] == "#" and (ni,nj) not in visited:
                visited.add((ni,nj))
                start_positions.append((ni,nj,step+1))
        
print(dfs(edges, start))
