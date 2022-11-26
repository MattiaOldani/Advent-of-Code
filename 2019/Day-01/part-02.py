# Solution: 4849444

with open("input.txt", "r") as f:
    fuel = f.readlines()

total = 0
for f in fuel:
    f = int(f.strip())
    while f > 0:
        f = int(f / 3) - 2
        total += f if f >= 0 else 0

print(total)
