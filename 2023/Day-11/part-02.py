# Solution: 702770569197

def expand(universe: list[str], galaxies: list[tuple[int,int]]) -> None:
    index = 0
    expanded_index = 0
    while index < len(universe):
        if universe[index].count("#") == 0:
            for i,galaxy in enumerate(galaxies):
                if galaxy[0] > expanded_index:
                    galaxies[i] = (galaxy[0] + 999999, galaxy[1])
            expanded_index += 1000000
        else:
            expanded_index += 1

        index += 1

    universe = [list(u) for u in universe]

    index = 0
    expanded_index = 0
    while index < len(universe[0]):
        column = "".join([universe[i][index] for i in range(len(universe))])
        if column.count("#") == 0:
            for i,galaxy in enumerate(galaxies):
                if galaxy[1] > expanded_index:
                    galaxies[i] = (galaxy[0], galaxy[1] + 999999)
            expanded_index += 1000000
        else:
            expanded_index += 1

        index += 1


with open("input.txt", "r") as f:
    universe = list(map(lambda x : list(x.strip()), f.readlines()))

galaxies = list()
for i,line in enumerate(universe):
    for j,cell in enumerate(line):
        if cell == "#":
            galaxies.append((i,j))

expand(universe, galaxies)

distances = 0
while len(galaxies) > 1:
    current = galaxies.pop()
    for other in galaxies:
        distances += abs(current[0] - other[0]) + abs(current[1] - other[1])

print(distances)
