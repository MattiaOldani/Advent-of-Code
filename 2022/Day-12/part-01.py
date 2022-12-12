# Solution: 449

with open("input.txt", "r") as f:
    grid = list(map(lambda x : [t for t in x.strip()], f.readlines()))

sx,sy = 0,0
ex,ey = 0,0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            sx,sy = i,j
            grid[i][j] = "a"
        elif grid[i][j] == "E":
            ex,ey = i,j
            grid[i][j] = "{"

visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
distance = [[2**16 for j in range(len(grid[0]))] for i in range(len(grid))]
distance[sx][sy] = 0

while True:
    i,j = 0,0
    min_ = -1
    for x in range(len(distance)):
        for y in range(len(distance[x])):
            if not visited[x][y] and (min_ == -1 or distance[x][y] < min_):
                min_ = distance[x][y]
                i,j = x,y
    
    if i > 0 and ord(grid[i-1][j]) - ord(grid[i][j]) < 2:
        if distance[i][j] + 1 < distance[i-1][j]:
            distance[i-1][j] = distance[i][j] + 1
            if grid[i-1][j] == "{":
                break

    if i < len(grid) - 1 and ord(grid[i+1][j]) - ord(grid[i][j]) < 2:
        if distance[i][j] + 1 < distance[i+1][j]:
            distance[i+1][j] = distance[i][j] + 1
            if grid[i+1][j] == "{":
                break

    if j > 0 and ord(grid[i][j-1]) - ord(grid[i][j]) < 2:
        if distance[i][j] + 1 < distance[i][j-1]:
            distance[i][j-1] = distance[i][j] + 1
            if grid[i][j-1] == "{":
                break

    if j < len(grid[i]) - 1 and ord(grid[i][j+1]) - ord(grid[i][j]) < 2:
        if distance[i][j] + 1 < distance[i][j+1]:
            distance[i][j+1] = distance[i][j] + 1
            if grid[i][j+1] == "{":
                break

    visited[i][j] = True

print(distance[ex][ey])
