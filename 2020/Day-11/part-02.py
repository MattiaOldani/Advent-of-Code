# Solution: 2121

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
            
            new_i = i-1
            while new_i >= 0 and grid[new_i][j] not in ["#", "L"]:
                new_i -= 1
            if new_i >= 0 and grid[new_i][j] == "#":
                adjacent += 1
            
            new_i = i+1
            while new_i <= len(grid)-1 and grid[new_i][j] not in ["#", "L"]:
                new_i += 1
            if new_i <= len(grid)-1 and grid[new_i][j] == "#":
                adjacent += 1
            
            new_j = j-1
            while new_j >= 0 and grid[i][new_j] not in ["#", "L"]:
                new_j -= 1
            if new_j >= 0 and grid[i][new_j] == "#":
                adjacent += 1
            
            new_j = j+1
            while new_j <= len(line)-1 and grid[i][new_j] not in ["#", "L"]:
                new_j += 1
            if new_j <= len(line)-1 and grid[i][new_j] == "#":
                adjacent += 1

            new_i = i-1
            new_j = j-1
            while new_i >= 0 and new_j >= 0 and grid[new_i][new_j] not in ["#", "L"]:
                new_i -= 1
                new_j -= 1
            if new_i >= 0 and new_j >= 0 and grid[new_i][new_j] == "#":
                adjacent += 1
            
            new_i = i-1
            new_j = j+1
            while new_i >= 0 and new_j <= len(line)-1 and grid[new_i][new_j] not in ["#", "L"]:
                new_i -= 1
                new_j += 1
            if new_i >= 0 and new_j <= len(line)-1 and grid[new_i][new_j] == "#":
                adjacent += 1

            new_i = i+1
            new_j = j-1
            while new_i <= len(grid)-1 and new_j >= 0 and grid[new_i][new_j] not in ["#", "L"]:
                new_i += 1
                new_j -= 1
            if new_i <= len(grid)-1 and new_j >= 0 and grid[new_i][new_j] == "#":
                adjacent += 1

            new_i = i+1
            new_j = j+1
            while new_i <= len(grid)-1 and new_j <= len(line)-1 and grid[new_i][new_j] not in ["#", "L"]:
                new_i += 1
                new_j += 1
            if new_i <= len(grid)-1 and new_j <= len(line)-1 and grid[new_i][new_j] == "#":
                adjacent += 1
            
            if grid[i][j] == "L" and adjacent == 0:
                changed = True
                new_line.append("#")
            elif grid[i][j] == "#" and adjacent >= 5:
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
