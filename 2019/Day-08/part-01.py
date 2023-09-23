# Solution: 2806

with open("input.txt", "r") as f:
    data = list(f.read().strip())

WIDTH = 25
HEIGHT = 6
STEP = WIDTH * HEIGHT

start = 0
min_zero = STEP
for i in range(0, len(data), STEP):
    current = min_zero
    min_zero = min(
        min_zero,
        len(list(
            filter(
                lambda x : x == "0",
                data[i : i + STEP]
            )
        ))
    )
    if current > min_zero:
        start = i

target = data[start : start + STEP]

one = len(list(filter(lambda x : x == "1", target)))
two = len(list(filter(lambda x : x == "2", target)))

print(one*two)
