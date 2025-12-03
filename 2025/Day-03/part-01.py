# Solution: 17346

with open("input.txt", "r") as f:
    batteries = [list(map(int, x.strip())) for x in f.readlines()]

count = 0
for b in batteries:
    max_value = max(b)
    index = b.index(max_value)

    if index == len(b) - 1:
        max_value = max(b[:-1])
        index = b.index(max_value)

    max_value = max_value * 10 + max(b[index + 1 :])
    count += max_value

print(count)
