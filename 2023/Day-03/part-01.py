# Solution: 556057

def find_symbol(i: int, j: int, grid: list) -> bool:
    if i > 0:
        if not grid[i-1][j].isdigit() and grid[i-1][j] != ".":
            return True
        if j > 0 and not grid[i-1][j-1].isdigit() and grid[i-1][j-1] != ".":
            return True
        if j < len(grid[0])-1 and not grid[i-1][j+1].isdigit() and grid[i-1][j+1] != ".":
            return True
    
    if i < len(grid)-1:
        if not grid[i+1][j].isdigit() and grid[i+1][j] != ".":
            return True
        if j > 0 and not grid[i+1][j-1].isdigit() and grid[i+1][j-1] != ".":
            return True
        if j < len(grid[0])-1 and not grid[i+1][j+1].isdigit() and grid[i+1][j+1] != ".":
            return True
    
    if j > 0 and not grid[i][j-1].isdigit() and grid[i][j-1] != ".":
        return True
    
    if j < len(grid[0])-1 and not grid[i][j+1].isdigit() and grid[i][j+1] != ".":
        return True
    
    return False


with open("input.txt", "r") as f:
    grid = list(map(lambda x: list(x.strip()), f.readlines()))

count = 0
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
            if find_symbol(i, j, grid):
                count += int("".join(line[start:end]))
                break

print(count)
