# Solution: 4355551200

def sium(r,c,grid):
    x,y = 0,0
    MOD = len(grid[0])
    
    counter = 0
    while x < len(grid)-1:
        for i in range(c):
            y = (y + 1) % MOD
        x += r
        if grid[x][y] == "#":
                counter += 1
    
    return counter


with open("input.txt", "r") as f:
    grid = list(map(lambda x : x.strip(), f.readlines()))

SLOPES = [
    [1,1],
    [3,1],
    [5,1],
    [7,1],
    [1,2]
]

counter = 1
for slope in SLOPES:
    counter *= sium(slope[1], slope[0], grid)
    
print(counter)
