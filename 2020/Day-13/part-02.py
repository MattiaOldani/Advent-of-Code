# Solution: 554865447501099

with open("input.txt", "r") as f:
    bus_IDs = [
        y
        for y in filter(
            lambda x: x[0] != "-",
            [
                ("-" if x == "x" else int(x), i)
                for i, x in enumerate(f.readlines()[1].split(","))
            ],
        )
    ]

cx, tx = 1, 0
for mod, add in bus_IDs:
    y = (-add - tx) % mod

    inv = pow(cx, mod - 2, mod)

    y = (y * inv) % mod

    tx = tx + cx * y
    cx *= mod

print(tx)
