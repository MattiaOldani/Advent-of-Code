# Solution: 113424

with open("input.txt", "r") as f:
    grid = list(map(lambda x : list(x.strip()), f.readlines()))

for i in range(1, len(grid)):
    line = grid[i]
    for j,element in enumerate(line):
        if element == "O":
            si = i-1
            while si >= 0 and grid[si][j] not in "O#":
                grid[si+1][j] = "."
                grid[si][j] = "O"
                si -= 1

count = 0
for i,line in enumerate(grid):
    rocks = "".join(line).count("O")
    count += rocks * (len(grid) - i)

print(count)
