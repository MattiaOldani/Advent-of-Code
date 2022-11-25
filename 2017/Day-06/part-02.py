# Solution: 1610

with open("input.txt", "r") as f:
    banks = f.readline().strip()

banks = list(map(lambda x : int(x), banks.split('\t')))

counter = 0
visited = [[b for b in banks]]
while True:
    max_ = max(banks)
    i = banks.index(max_)

    blocks = banks[i]
    banks[i] = 0

    i = (i + 1) % len(banks)
    for b in range(blocks):
        banks[i] += 1
        i = (i + 1) % len(banks)

    counter += 1

    if banks in visited:
        print(counter - visited.index(banks))
        break

    visited.append([b for b in banks])
