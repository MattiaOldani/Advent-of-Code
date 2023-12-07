# Solution: 81956384

with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

seeds = list(map(int, data.pop(0).split(" ")))
seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

for block in data:
    block = block.strip().split("\n")[1:]
    
    ranges = list()
    for line in block:
        ranges.append(list(map(int, line.split(" "))))
    
    new_seeds = list()
    while len(seeds) > 0:
        seed_start, seed_end = seeds.pop()
        for dst, src, rng in ranges:
            overlap_start = max(src, seed_start)
            overlap_end = min(src + rng, seed_end)
            if overlap_start < overlap_end:
                new_seeds.append((overlap_start + dst - src, overlap_end + dst - src))
                if seed_start < overlap_start:
                    seeds.append((seed_start, overlap_start))
                if overlap_end < seed_end:
                    seeds.append((overlap_end, seed_end))
                break
        else:
            new_seeds.append((seed_start, seed_end))

    seeds = new_seeds

print(min(seeds)[0])
