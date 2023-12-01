# Solution: 2275

with open("input.txt", "r") as f:
    grid = list(map(lambda x : list(x.strip()), f.readlines()))

while True:
    new_grid = list()
    changed = False
    for i in range(len(grid)):
        new_line = list()
        line = grid[i]
        for j in range(len(line)):
            if grid[i][j] == ".":
                new_line.append(".")
                continue
            
            adjacent = 0
            
            if i > 0:
                adjacent += 1 if grid[i-1][j] == "#" else 0
                if j > 0 and grid[i-1][j-1] == "#":
                    adjacent += 1
                if j < len(line) - 1 and grid[i-1][j+1] == "#":
                    adjacent += 1
            
            if i < len(grid) - 1:
                adjacent += 1 if grid[i+1][j] == "#" else 0
                if j > 0 and grid[i+1][j-1] == "#":
                    adjacent += 1
                if j < len(line) - 1 and grid[i+1][j+1] == "#":
                    adjacent += 1
            
            if j > 0 and grid[i][j-1] == "#":
                adjacent += 1
            
            if j < len(line) - 1 and grid[i][j+1] == "#":
                adjacent += 1
            
            if grid[i][j] == "L" and adjacent == 0:
                changed = True
                new_line.append("#")
            elif grid[i][j] == "#" and adjacent >= 4:
                changed = True
                new_line.append("L")
            else:
                new_line.append(grid[i][j])
        
        new_grid.append(new_line)
    
    if not changed:
        break
    
    grid = new_grid.copy()

count = 0
for line in grid:
    count += len(list(filter(lambda x : x == "#", line)))

print(count)
