# Solution: 217443

from collections import defaultdict


with open("input.txt", "r") as f:
    data = [int(x) for x in f.readline().split()]


stones = defaultdict(lambda: 0)
for stone in data:
    stones[stone] += 1

for _ in range(25):
    items = list(stones.items())
    for stone, n in items:
        if stone == 0:
            stones[1] += n
            stones[0] -= n
            continue
        if len(str(stone)) % 2 == 0:
            power = 10 ** (len(str(stone)) // 2)
            left = stone // power
            right = stone % power
            stones[left] += n
            stones[right] += n
            stones[stone] -= n
            continue
        stones[stone * 2024] += n
        stones[stone] -= n

print(sum(stones.values()))
