# Solution: 781

def turn_corners_on(grid: list) -> None:
    grid[0][0] = "#"
    grid[0][len(grid[0]) - 1] = "#"
    grid[len(grid) - 1][0] = "#"
    grid[len(grid) - 1][len(grid[0]) - 1] = "#"


with open("input.txt", "r") as f:
    grid = list(map(lambda x : list(x.strip()), f.readlines()))

turn_corners_on(grid)

for _ in range(100):
    grid_after_step = list()
    for i in range(len(grid)):
        line = list()
        for j in range(len(grid[i])):
            count = 0
            if i > 0:
                count += 1 if grid[i-1][j] == "#" else 0
                if j > 0:
                    count += 1 if grid[i-1][j-1] == "#" else 0
                if j < len(grid[i]) - 1:
                    count += 1 if grid[i-1][j+1] == "#" else 0
            if i < len(grid) - 1:
                count += 1 if grid[i+1][j] == "#" else 0
                if j > 0:
                    count += 1 if grid[i+1][j-1] == "#" else 0
                if j < len(grid[i]) - 1:
                    count += 1 if grid[i+1][j+1] == "#" else 0
            if j > 0:
                count += 1 if grid[i][j-1] == "#" else 0
            if j < len(grid[i]) - 1:
                count += 1 if grid[i][j+1] == "#" else 0

            if grid[i][j] == "#":
                line.append("#" if 2 <= count <= 3 else ".")
            else:
                line.append("#" if count == 3 else ".")
        
        grid_after_step.append(line)
    
    for i,line in enumerate(grid_after_step):
        grid[i] = line.copy()
    turn_corners_on(grid)

count = 0
for line in grid:
    for char in line:
        count += 1 if char == "#" else 0

print(count)
