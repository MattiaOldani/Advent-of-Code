# Solution: 2545

with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]


count = 0
for i, line in enumerate(grid):
    words = []

    words += ["".join(line[j : j + 4]) for j in range(len(line) - 3)]

    for j in range(len(line)):
        if i >= 3:
            words += ["".join([grid[i - t][j] for t in range(4)])]
            if j >= 3:
                words += ["".join([grid[i - t][j - t] for t in range(4)])]
            if j <= len(line) - 4:
                words += ["".join([grid[i - t][j + t] for t in range(4)])]

    count += len(list(filter(lambda x: x in ["XMAS", "SAMX"], words)))

print(count)
