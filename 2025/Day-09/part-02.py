# Solution: 1568849600


def fall_in_bounds(path, v1, v2):
    min_x = min(v1[0], v2[0])
    max_x = max(v1[0], v2[0])
    min_y = min(v1[1], v2[1])
    max_y = max(v1[1], v2[1])

    for i in range(len(path) - 1):
        o1 = path[i]
        o2 = path[i + 1]

        if o1[0] == o2[0]:
            pts = [(o1[0], y) for y in range(min(o1[1], o2[1]), max(o1[1], o2[1]) + 1)]
        else:
            pts = [(x, o1[1]) for x in range(min(o1[0], o2[0]), max(o1[0], o2[0]) + 1)]

        if any([min_x < x[0] < max_x and min_y < x[1] < max_y for x in pts]):
            return True

    return False


with open("input.txt", "r") as f:
    vertex = [tuple(map(int, x.strip().split(","))) for x in f.readlines()]

max_area = 0
for i, v1 in enumerate(vertex):
    for j, v2 in enumerate(vertex):
        if j <= i:
            continue

        x1, y1 = v1
        x2, y2 = v2

        if j == i + 1:
            max_area = max(max_area, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))
            continue

        current = vertex[i : j + 1]
        opposite = vertex[: i + 1][::-1] + vertex[j:][::-1]

        if not fall_in_bounds(current, v1, v2) and not fall_in_bounds(opposite, v1, v2):
            max_area = max(max_area, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

print(max_area)
