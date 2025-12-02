# Solution: 38731915928

from math import ceil


with open("input.txt", "r") as f:
    ranges = [x.strip().split("-") for x in f.read().strip().split(",")]

count = 0
for first, second in ranges:
    half = ceil(len(second) / 2)
    first_half = int(second[:half])

    first = int(first)
    second = int(second)

    visited = set()
    while first_half > 0:
        current = str(first_half)
        while int(current) < first:
            current += str(first_half)

        while int(current) <= second:
            if int(current) not in visited:
                count += int(current)
                visited.add(int(current))
            current += str(first_half)

        first_half -= 1

print(count)
