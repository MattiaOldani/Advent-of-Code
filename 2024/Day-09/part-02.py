# Solution: 6488291456470

from functools import reduce


with open("input.txt", "r") as f:
    data = list(map(int, f.readline().strip()))


memory = []
for i, cell in enumerate(data):
    memory += [(i // 2 if i % 2 == 0 else ".", cell)]

max_ID = (len(data) - 1) // 2
for i in range(max_ID, -1, -1):
    block_position = [m[0] for m in memory].index(i)
    block_ID, block_dimension = memory[block_position]

    space_position = -1
    for t, (cell_ID, count) in enumerate(memory[:block_position]):
        if cell_ID == "." and count >= block_dimension:
            space_position = t
            break

    if space_position == -1:
        continue

    space_dimension = memory[space_position][1]

    memory[block_position] = (".", block_dimension)
    memory.insert(space_position, (block_ID, block_dimension))
    memory[space_position + 1] = (".", space_dimension - block_dimension)

memory = reduce(lambda x, y: x + y, [[m[0] for _ in range(m[1])] for m in memory], [])

count = 0
for index, cell in enumerate(memory):
    if cell == ".":
        continue
    count += index * cell

print(count)
