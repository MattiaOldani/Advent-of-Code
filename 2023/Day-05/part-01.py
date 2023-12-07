# Solution: 218513636

with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

seeds = list(map(int, data.pop(0).split(" ")))

for block in data:
    block = block.strip().split("\n")[1:]

    ranges = list()
    for line in block:
        ranges.append(list(map(int, line.split(" "))))
    
    for i,seed in enumerate(seeds):
        for dst, src, rng in ranges:
            if src <= seed < src + rng:
                seeds[i] = dst + seed - src
                break
    
print(min(seeds))
