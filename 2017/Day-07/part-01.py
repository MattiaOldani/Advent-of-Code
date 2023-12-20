# Solution: eugwuhl

with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(), f.readlines()))

for line in data:
    name = line[0]

    if len(line[2:]) == 0:
        continue

    if all([name not in other[2:] for other in data]):
        print(name)
        break
