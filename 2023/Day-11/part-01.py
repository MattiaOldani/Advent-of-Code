# Solution: 9974721

def expand(universe: list[str]) -> list[list[str]]:
    i = 0
    while i < len(universe):
        if universe[i].count("#") == 0:
            universe.insert(i, "." * len(universe[i]))
            i += 2
        else:
            i += 1

    universe = [list(u) for u in universe]

    j = 0
    while j < len(universe[0]):
        column = "".join([universe[i][j] for i in range(len(universe))])
        if column.count("#") == 0:
            for i in range(len(universe)):
                universe[i].insert(j, ".")
            j += 2
        else:
            j += 1
    
    return universe


with open("input.txt", "r") as f:
    universe = list(map(lambda x : x.strip(), f.readlines()))

universe = expand(universe)

galaxies = list()
for i,line in enumerate(universe):
    for j,cell in enumerate(line):
        if cell == "#":
            galaxies.append((i,j))

distances = 0
while len(galaxies) > 1:
    current = galaxies.pop()
    for other in galaxies:
        distances += abs(current[0] - other[0]) + abs(current[1] - other[1])

print(distances)
