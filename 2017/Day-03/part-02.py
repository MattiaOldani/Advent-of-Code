# Solution: 369601

with open("input.txt", "r") as f:
    end = int(f.readline().strip())

direction = -1

#FACE = [[1,0], [0,1], [-1,0], [0,-1]]

i,j,step = 0,0,1
counter = 0
start = 1

grid = [
    [1]
]

while start < end:
    direction = (direction + 1) % 4

    x = 0
    while x < step and start < end:
        match direction:
            case 0:
                j += 1
                if j == len(grid[i]):
                    for line in grid:
                        line.append(0)
                grid[i][j] = grid[i][j-1]
                if i-1 >= 0:
                    grid[i][j] += grid[i-1][j]
                    if j-1 >= 0:
                        grid[i][j] += grid[i-1][j-1]
                    if j+1 < len(grid[i-1]):
                        grid[i][j] += grid[i-1][j+1]
                start = grid[i][j]
            
            case 1:
                i -= 1
                if i == -1:
                    grid.insert(0, [0 for l in range(len(grid[0]))])
                    i = 0
                grid[i][j] = grid[i+1][j]
                if j-1 >= 0:
                    grid[i][j] += grid[i][j-1]
                    if i-1 >= 0:
                        grid[i][j] += grid[i-1][j-1]
                    if i+1 < len(grid):
                        grid[i][j] += grid[i+1][j-1]
                start = grid[i][j]

            case 2:
                j -= 1
                if j == -1:
                    for line in grid:
                        line.insert(0, 0)
                    j = 0
                grid[i][j] = grid[i][j+1]
                if i+1 < len(grid):
                    grid[i][j] += grid[i+1][j]
                    if j-1 >= 0:
                        grid[i][j] += grid[i+1][j-1]
                    if j+1 < len(grid[i+1]):
                        grid[i][j] += grid[i+1][j+1]
                start = grid[i][j]

            case 3:
                i += 1
                if i == len(grid):
                    grid.append([0 for l in range(len(grid[0]))])
                grid[i][j] = grid[i-1][j]
                if j+1 < len(grid[i]):
                    grid[i][j] += grid[i][j+1]
                    if i-1 >= 0:
                        grid[i][j] += grid[i-1][j+1]
                    if i+1 < len(grid):
                        grid[i][j] += grid[i+1][j+1]
                start = grid[i][j]

        x += 1

    counter += 1

    if counter == 2:
        step += 1
        counter = 0

print(start)
