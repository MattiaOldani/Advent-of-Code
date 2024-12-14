# Solution: 225521010

from functools import reduce


with open("input.txt", "r") as f:
    guards = [[int(y) for y in x.strip().split()] for x in f.readlines()]


HEIGHT = 103
WIDTH = 101

for i in range(len(guards)):
    px, py, vx, vy = guards[i]
    px = (px + 100 * vx) % WIDTH
    py = (py + 100 * vy) % HEIGHT

    guards[i] = (py, px)

quadrants = [
    [(0, HEIGHT // 2), (0, WIDTH // 2)],
    [(0, HEIGHT // 2), (WIDTH // 2 + 1, WIDTH)],
    [(HEIGHT // 2 + 1, HEIGHT), (0, WIDTH // 2)],
    [(HEIGHT // 2 + 1, HEIGHT), (WIDTH // 2 + 1, WIDTH)],
]

print(
    reduce(
        lambda x, y: x * y,
        [
            len(
                list(
                    filter(
                        lambda g: g[0] in range(*q[0]) and g[1] in range(*q[1]), guards
                    )
                )
            )
            for q in quadrants
        ],
        1,
    )
)
