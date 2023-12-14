# Solution: 96003

def cycle(grid: list[list[str]]) -> None:
    for _ in range(4):
        roll(grid)
        rotate(grid)


def roll(grid: list[list[str]]) -> None:
    for i in range(1, len(grid)):
        line = grid[i]
        for j,element in enumerate(line):
            if element == "O":
                si = i-1
                while si >= 0 and grid[si][j] not in "O#":
                    grid[si+1][j] = "."
                    grid[si][j] = "O"
                    si -= 1


def rotate(grid: list[list[str]]) -> None:
    size = len(grid)
    
    for i in range(size):
        for j in range(i):
            grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
    
    for i in range(size):
        for j in range(size // 2):
            grid[i][j], grid[i][size-j-1] = grid[i][size-j-1], grid[i][j]


with open("input.txt", "r") as f:
    grid = list(map(lambda x : list(x.strip()), f.readlines()))

first_hash = hash("".join(["".join(line) for line in grid]))
hash_cycle = {first_hash : 0}

counter = 0
while counter < 1000000000:
    cycle(grid)
    counter += 1
    
    current_hash = hash("".join(["".join(line) for line in grid]))
    if current_hash in hash_cycle:
        difference = counter - hash_cycle[current_hash]
        counter += difference * ((1000000000 - counter) // difference)
        while counter < 1000000000:
            cycle(grid)
            counter += 1
    
    hash_cycle[current_hash] = counter

count = 0
for i,line in enumerate(grid):
    rocks = "".join(line).count("O")
    count += rocks * (len(grid) - i)

print(count)
