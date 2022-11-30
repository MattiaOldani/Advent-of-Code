# Solution: 280

with open("input.txt", "r") as f:
    grid = list(map(lambda x : x.strip(), f.readlines()))

x,y = 0,0
counter = 0
MOD = len(grid[0])

while x < len(grid)-1:
    for i in range(3):
        y = (y + 1) % MOD
    x += 1
    if grid[x][y] == "#":
            counter += 1
    
print(counter)
