# Solution: 914966


def bfs(grid: list[list[str]], i: int, j: int):
    visited = set([(i, j)])
    to_check = set([(i, j)])

    edges = []

    letter = grid[i][j]
    while len(to_check) > 0:
        i, j = to_check.pop()

        if (i - 1, j) not in visited:
            if i > 0 and grid[i - 1][j] == letter:
                visited.add((i - 1, j))
                to_check.add((i - 1, j))
            else:
                edges += [[(i - 1, j - 1), (i - 1, j)]]

        if (i, j + 1) not in visited:
            if j < len(grid[0]) - 1 and grid[i][j + 1] == letter:
                visited.add((i, j + 1))
                to_check.add((i, j + 1))
            else:
                edges += [[(i - 1, j), (i, j)]]

        if (i + 1, j) not in visited:
            if i < len(grid) - 1 and grid[i + 1][j] == letter:
                visited.add((i + 1, j))
                to_check.add((i + 1, j))
            else:
                edges += [[(i, j), (i, j - 1)]]

        if (i, j - 1) not in visited:
            if j > 0 and grid[i][j - 1] == letter:
                visited.add((i, j - 1))
                to_check.add((i, j - 1))
            else:
                edges += [[(i, j - 1), (i - 1, j - 1)]]

    components = []

    component = [edges.pop()]
    for i in range(len(edges)):
        if edges[i] == component[0]:
            edges = edges[:i] + edges[i + 1 :]
            break

    while len(edges) > 0:
        current_len = len(edges)
        _, end_c = component[-1]
        for edge in edges:
            start_e, _ = edge
            if end_c == start_e:
                start_c, end_c = component[-1][0]
                start_e, end_e = edge[1]
                if start_c == start_e:
                    facing = "R" if end_e > end_c else "L"
                    if facing == "R":
                        if (start_e + 1, end_e) in visited:
                            component += [edge]
                            edges.remove(edge)
                            break
                        else:
                            continue
                    else:
                        if (start_e, end_e + 1) in visited:
                            component += [edge]
                            edges.remove(edge)
                            break
                        else:
                            continue
                elif end_c == end_e:
                    facing = "U" if start_e < start_c else "D"
                    if facing == "U":
                        if (start_e + 1, end_e + 1) in visited:
                            component += [edge]
                            edges.remove(edge)
                            break
                        else:
                            continue
                    else:
                        if (start_e, end_e) in visited:
                            component += [edge]
                            edges.remove(edge)
                            break
                        else:
                            continue
                else:
                    component += [edge]
                    edges.remove(edge)
                    break

        if current_len == len(edges):
            components += [component]

            component = [edges.pop()]
            for i in range(len(edges)):
                if edges[i] == component[0]:
                    edges = edges[:i] + edges[i + 1 :]
                    break

    components += [component]

    no_duplicates_components = []
    for component in components:
        no_duplicates_component = []
        for start, _ in component:
            no_duplicates_component += [start]
        no_duplicates_components += [no_duplicates_component]

    return visited, no_duplicates_components


def full_perimeter(components: list) -> int:
    return sum([perimeter(x) for x in components])


def perimeter(edges: list) -> int:
    if edges[0][0] == edges[1][0]:
        facing = "H"
    else:
        facing = "V"

    i = 0
    while True:
        ci, cj = edges[0]
        ni, nj = edges[1]
        if ci == ni and facing == "V":
            facing = "H"
            break
        if cj == nj and facing == "H":
            facing = "V"
            break
        edges += [edges.pop(0)]

    edges += [edges[0]]

    facing = "V" if edges[0][1] == edges[1][1] else "H"

    side = 1
    for i in range(len(edges) - 1):
        ci, cj = edges[i]
        ni, nj = edges[i + 1]

        if ci == ni and facing == "V":
            side += 1
            facing = "H"
            continue
        if cj == nj and facing == "H":
            side += 1
            facing = "V"
            continue

    return side


with open("input.txt", "r") as f:
    grid = [list(x.strip()) for x in f.readlines()]


to_visit = set([(i, j) for i in range(len(grid)) for j in range(len(grid[0]))])

count = 0
while len(to_visit) > 0:
    i, j = to_visit.pop()
    visited, components = bfs(grid, i, j)
    count += len(visited) * full_perimeter(components)
    to_visit.difference_update(visited)

print(count)
