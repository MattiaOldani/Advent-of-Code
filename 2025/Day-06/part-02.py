# Solution: 10227753257799

from functools import reduce


def exec_operation(numbers, operation):
    return (
        reduce(lambda x, y: x + y, numbers, 0)
        if operation == "+"
        else reduce(lambda x, y: x * y, numbers, 1)
    )


with open("input.txt", "r") as f:
    data = [list(x.rstrip("\n") + " ") for x in f.readlines()]

count = 0

numbers = []
operation = None
for column in zip(*data):
    column = list(map(lambda x: x.strip(), column))

    if all([x == "" for x in column]):
        count += exec_operation(numbers, operation)
        numbers = []
        operation = None
        continue

    operation = operation or column[-1]
    numbers += [int("".join(column[:-1]))]

print(count)
