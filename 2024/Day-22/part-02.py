# Solution: 1499

from collections import defaultdict


with open("input.txt", "r") as f:
    starters = [int(x.strip()) for x in f.readlines()]

differences = defaultdict(lambda: [])
for starter in starters:
    values = [starter % 10]
    sequence = []
    for _ in range(2000):
        starter = ((starter * 64) ^ starter) % 16777216
        starter = ((starter // 32) ^ starter) % 16777216
        starter = ((starter * 2048) ^ starter) % 16777216
        values += [starter % 10]
        sequence += [values[-1] - values[-2]]

    backup = defaultdict(lambda: [])
    for i in range(len(sequence) - 3):
        window = sequence[i : i + 4]
        backup[tuple(window)] += [values[i + 4]]

    for sequence, values in backup.items():
        differences[sequence] += [values[0]]

count = 0
for values in differences.values():
    count = max(count, sum(values))

print(count)
