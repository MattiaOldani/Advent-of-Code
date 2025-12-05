# Solution: 334714395325710

with open("input.txt", "r") as f:
    ranges = list(
        sorted(
            [
                list(map(int, x.strip().split("-")))
                for x in f.read().strip().split("\n\n")[0].split("\n")
            ],
            key=lambda x: x[0],
        )
    )

i = 0
count = 0
while i < len(ranges) - 1:
    start_i, end_i = ranges[i]

    index = i + 1
    while index < len(ranges):
        start_j, end_j = ranges[index]

        if start_j > end_i:
            break

        end_i = max(end_i, end_j)
        ranges.remove(ranges[index])

    i += 1
    count += end_i - start_i + 1

print(count)
