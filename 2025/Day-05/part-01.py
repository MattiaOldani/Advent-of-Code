# Solution: 848

with open("input.txt", "r") as f:
    data = [x.strip().split("\n") for x in f.read().strip().split("\n\n")]

ranges = [list(map(int, x.split("-"))) for x in data[0]]
IDs = list(map(int, data[1]))

count = 0
for ID in IDs:
    for start, end in ranges:
        if start <= ID <= end:
            count += 1
            break

print(count)
