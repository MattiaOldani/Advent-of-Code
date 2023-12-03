# Solution: 82824352

def find_gear(i: int, j: int, grid: list) -> tuple:
    if i > 0:
        if grid[i-1][j] == "*":
            return (True, (i-1,j))
        if j > 0 and grid[i-1][j-1] == "*":
            return (True, (i-1,j-1))
        if j < len(grid[0])-1 and grid[i-1][j+1] == "*":
            return (True, (i-1,j+1))
    
    if i < len(grid)-1:
        if grid[i+1][j] == "*":
            return (True, (i+1,j))
        if j > 0 and grid[i+1][j-1] == "*":
            return (True, (i+1,j-1))
        if j < len(grid[0])-1 and grid[i+1][j+1] == "*":
            return (True, (i+1,j+1))
    
    if j > 0 and grid[i][j-1] == "*":
        return (True, (i,j-1))
    
    if j < len(grid[0])-1 and grid[i][j+1] == "*":
        return (True, (i,j+1))
    
    return (False, ())


with open("input.txt", "r") as f:
    grid = list(map(lambda x: list(x.strip()), f.readlines()))

gear = dict()
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "*":
            gear[(i,j)] = []

for i,line in enumerate(grid):
    t = 0
    while t < len(line):
        if not line[t].isdigit():
            t += 1
            continue
        k = t + 1
        while k < len(line) and line[k].isdigit():
            k += 1
        start = t
        end = k
        t = k
        for j in range(start, end):
            find, coordinates = find_gear(i, j, grid)
            if find:
                gear[coordinates].append(int("".join(line[start:end])))
                break

count = 0
valid = [g for g in gear.values() if len(g) == 2]
for couple in valid:
    count += (couple[0] * couple[1])

print(count)
