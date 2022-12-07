# Solution: 1613415325809

with open("input.txt", "r") as f:
    start = list(map(int, f.readline().strip().split(",")))

fish = [[i,0] for i in range(9)]
fish = dict(fish)

for n in start:
    fish[n] += 1

for i in range(256):
    zero = fish[0]
    for t in range(1,9):
        fish[t-1] = fish[t]
    fish[8] = zero
    fish[6] += zero

total = list(map(lambda x : x[1], fish.items()))
print(sum(total))
