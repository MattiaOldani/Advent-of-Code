# Solution: 3619


def get_heights(grid: list[list[str]]):
    heights = []

    for j in range(len(grid[0])):
        i = 1
        while grid[i][j] == "#":
            i += 1
        heights += [i - 1]

    return heights


with open("input.txt", "r") as f:
    data = [[list(y) for y in x.strip().split("\n")] for x in f.read().split("\n\n")]


TARGET = len(data[0]) - 2

locks = [get_heights(y) for y in filter(lambda x: x[0][0] == "#", data)]
keys = [get_heights(y[::-1]) for y in filter(lambda x: x[0][0] == ".", data)]

count = 0
for key in keys:
    for lock in locks:
        union = [key[i] + lock[i] for i in range(len(key))]
        if all([union[i] <= TARGET for i in range(len(union))]):
            count += 1

print(count)
