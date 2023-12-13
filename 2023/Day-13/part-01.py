# Solution: 34993

def find_reflection(grid: list[str], multiplier: int) -> int:
    for j in range(len(grid[0])-1):
        size = min(j+1, len(grid[0])-j-1)
        for line in grid:
            if size == j+1:
                pattern = [line[j-t] == line[j+t+1] for t in range(size)]
            else:
                start = len(grid[0]) - size - 1
                pattern = [line[start-t] == line[start+t+1] for t in range(size)]
            
            if not all(pattern):
                break
        else:
            return multiplier * (j+1)
    
    return 0


with open("input.txt", "r") as f:
    grids = list(map(lambda x : x.strip().split("\n"), f.read().split("\n\n")))

count = 0
for grid in grids:
    count += find_reflection(grid, 1)
    grid = ["".join([grid[i][j] for i in range(len(grid))]) for j in range(len(grid[0]))]
    count += find_reflection(grid, 100)

print(count)
