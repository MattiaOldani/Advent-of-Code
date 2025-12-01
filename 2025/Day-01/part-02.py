# Solution: 6599

with open("input.txt", "r") as f:
    rotations = [
        (-1 if x.strip()[0] == "L" else 1, int(x.strip()[1:])) for x in f.readlines()
    ]

dial = 50
count = 0
for direction, amount in rotations:
    for _ in range(amount):
        dial = (dial + direction) % 100
        if dial == 0:
            count += 1

print(count)
