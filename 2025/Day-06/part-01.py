# Solution: 5227286044585

from functools import reduce


with open("input.txt", "r") as f:
    data = [
        list(filter(lambda x: len(x) > 0, x.strip().split())) for x in f.readlines()
    ]

count = 0
columns = zip(*data)
for column in columns:
    operation = column[-1]
    numbers = map(int, column[:-1])
    if operation == "+":
        count += reduce(lambda x, y: x + y, numbers, 0)
    else:
        count += reduce(lambda x, y: x * y, numbers, 1)

print(count)
