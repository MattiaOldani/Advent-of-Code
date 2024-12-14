# Solution: 7774

with open("input.txt", "r") as f:
    guards = [[int(y) for y in x.strip().split()] for x in f.readlines()]


i = 0
steps = set()
while True:
    x = 101 * i + 98
    y = 103 * i + 49

    if x in steps:
        step = x
        break
    if y in steps:
        step = y
        break

    steps.add(x)
    steps.add(y)

    i += 1

HEIGHT = 103
WIDTH = 101

for i in range(len(guards)):
    px, py, vx, vy = guards[i]
    px = (px + step * vx) % WIDTH
    py = (py + step * vy) % HEIGHT

    guards[i] = (py, px)

grid = [
    "".join(["#" if (y, x) in guards else "." for x in range(WIDTH)])
    for y in range(HEIGHT)
]

print(step, "\n")
for line in grid:
    print(line)
