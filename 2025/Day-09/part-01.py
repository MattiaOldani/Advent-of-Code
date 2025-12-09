# Solution: 4754955192

with open("input.txt", "r") as f:
    vertex = [list(map(int, x.strip().split(","))) for x in f.readlines()]

max_area = 0
for i, v1 in enumerate(vertex):
    x1, y1 = v1
    for x2, y2 in vertex[i + 1 :]:
        max_area = max(max_area, (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1))

print(max_area)
