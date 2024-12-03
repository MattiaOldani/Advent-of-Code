# Solution: 174336360

import re


with open("input.txt", "r") as f:
    data = f.readlines()

count = 0
for line in data:
    valids = re.findall(r"mul\(([0-9]+,[0-9]+)\)", line)
    for valid in valids:
        a, b = map(int, valid.split(","))
        count += a * b

print(count)
