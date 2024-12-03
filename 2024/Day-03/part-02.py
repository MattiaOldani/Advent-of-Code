# Solution: 88802350

import re


with open("input.txt", "r") as f:
    data = f.readlines()

count = 0
to_count = True
for line in data:
    valids = [
        list(filter(lambda y: len(y) > 0, x))[0]
        for x in re.findall(r"(mul\([0-9]+,[0-9]+\))|(do\(\))|(don\'t\(\))", line)
    ]

    for valid in valids:
        match valid:
            case "do()":
                to_count = True
            case "don't()":
                to_count = False
            case _:
                a, b = map(int, valid[4:-1].split(","))
                count += a * b * to_count

print(count)
