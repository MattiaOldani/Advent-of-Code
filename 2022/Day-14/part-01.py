# Solution: 979

with open("input.txt", "r") as f:
    rocks = list(map(lambda x : x.strip().split(" -> "), f.readlines()))

bounds = set()
waterfall = dict()
for rock in rocks:
    rock = list(map(lambda x : [int(x.split(",")[0]), int(x.split(",")[1])], rock))
    for i in range(1,len(rock)):
        prev = rock[i-1]
        curr = rock[i]
        if prev[0] == curr[0]:
            y = [t for t in range(min(prev[1],curr[1]), max(prev[1],curr[1])+1)]
            x = [prev[0]] * len(y)
        else:
            x = [t for t in range(min(prev[0],curr[0]), max(prev[0],curr[0])+1)]
            y = [prev[1]] * len(x)
        for t in range(len(x)):
            waterfall[(x[t],y[t])] = 0
            bounds.add(y[t])

bound = max(bounds)

total = 0
fall = False
while not fall:
    rest = False
    sx,sy = 500,0
    while not rest and not fall:
        if (sx,sy+1) in waterfall:
            if (sx-1,sy+1) in waterfall:
                if (sx+1,sy+1) in waterfall:
                    rest = True
                    total += 1
                    waterfall[(sx,sy)] = 0
                else:
                    sx += 1
                    sy += 1
            else:
                sx -= 1
                sy += 1
        else:
            sy += 1

        if sy == bound:
            fall = True    

print(total)
