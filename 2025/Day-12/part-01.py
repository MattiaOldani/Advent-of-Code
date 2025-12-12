# Solution: 567

from functools import reduce


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

dimensions = list(map(int, data.pop(0).split()))

count = 0
for line in data[0].strip().split("\n"):
    line = line.split()

    d1, d2 = list(map(int, line.pop(0)[:-1].split("x")))

    presents = list(map(int, line))

    if reduce(lambda x, y: x + y[0] * y[1], zip(presents, dimensions), 0) > d1 * d2:
        continue

    if sum(presents) - (d1 // 3) * (d2 // 3) <= 0:
        count += 1

print(count)
