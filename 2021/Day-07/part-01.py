# Solution: 356922

with open("input.txt", "r") as f:
    position = list(map(int, f.readline().strip().split(",")))

position.sort()

cost = 0
for i in range(position[0], position[len(position)-1]+1):
    total = 0
    for p in position:
        total += abs(i-p)
    
    if cost == 0 or total < cost:
        cost = total

print(cost)
