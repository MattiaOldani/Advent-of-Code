# Solution: 232


def check_neighbors(to_check, active_cube, accept):
    new_cube = set()
    for cell in to_check:
        active = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for t in [-1, 0, 1]:
                    if i == j == t == 0:
                        continue

                    ci, cj, ct = cell
                    if (ci + i, cj + j, ct + t) in active_cube:
                        active += 1

        if accept(active):
            new_cube.add(cell)

    return new_cube


with open("input.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]


cube = set()
for i, line in enumerate(data):
    for j, cell in enumerate(line):
        if cell == "#":
            cube.add((i, j, 0))

for _ in range(6):
    new_cube = check_neighbors(cube, cube, lambda x: 2 <= x <= 3)

    ii = [c[0] for c in cube]
    min_i, max_i = min(ii) - 1, max(ii) + 2
    jj = [c[1] for c in cube]
    min_j, max_j = min(jj) - 1, max(jj) + 2
    tt = [c[2] for c in cube]
    min_t, max_t = min(tt) - 1, max(tt) + 2

    other = set(
        (i, j, t)
        for i in range(min_i, max_i)
        for j in range(min_j, max_j)
        for t in range(min_t, max_t)
    )

    other.difference_update(cube)

    cube = new_cube.union(check_neighbors(other, cube, lambda x: x == 3))

print(len(cube))
