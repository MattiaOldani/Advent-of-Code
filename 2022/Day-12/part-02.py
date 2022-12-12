# Solution: 443

with open("input.txt", "r") as f:
    grid = list(map(lambda x : [t for t in x.strip()], f.readlines()))

sx,sy = 0,0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            grid[i][j] = "a"
        elif grid[i][j] == "E":
            grid[i][j] = "z"
            sx,sy = i,j

visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
distance = [[2**16 for j in range(len(grid[0]))] for i in range(len(grid))]
distance[sx][sy] = 0

found = False
while not found:
    i,j = 0,0
    min_ = -1
    for x in range(len(distance)):
        for y in range(len(distance[x])):
            if not visited[x][y] and (min_ == -1 or distance[x][y] < min_):
                min_ = distance[x][y]
                i,j = x,y
    
    end = list()
    if i > 0 and ord(grid[i][j]) - ord(grid[i-1][j]) < 2:
        if distance[i][j] + 1 < distance[i-1][j]:
            end.append([i-1, j])
            distance[i-1][j] = distance[i][j] + 1

    if i < len(grid) - 1 and ord(grid[i][j]) - ord(grid[i+1][j]) < 2:
        if distance[i][j] + 1 < distance[i+1][j]:
            end.append([i+1, j])
            distance[i+1][j] = distance[i][j] + 1

    if j > 0 and ord(grid[i][j]) - ord(grid[i][j-1]) < 2:
        if distance[i][j] + 1 < distance[i][j-1]:
            end.append([i, j-1])
            distance[i][j-1] = distance[i][j] + 1
            
    if j < len(grid[i]) - 1 and ord(grid[i][j]) - ord(grid[i][j+1]) < 2:
        if distance[i][j] + 1 < distance[i][j+1]:
            end.append([i, j+1])
            distance[i][j+1] = distance[i][j] + 1

    for couple in end:
        x,y = couple
        if grid[x][y] == "a":
            print(distance[x][y])
            found = True
            break

    visited[i][j] = True
