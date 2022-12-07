# Solution: 

with open("input.txt", "r") as f:
    lines = list(map(lambda x : x.strip().split(" "), f.readlines()))

points = dict()
for line in lines:
    x1,y1,x2,y2 = list(map(int, line))

    if x1 == x2:
        step = 1 if y2 > y1 else -1
        for i in range(y1, y2+step, step):
            try:
                points[(x1,i)] += 1
            except:
                points[(x1,i)] = 1
    elif y1 == y2:
        step = 1 if x2 > x1 else -1
        for i in range(x1, x2+step, step):
            try:
                points[(i,y1)] += 1
            except:
                points[(i,y1)] = 1
    
overlap = list(map(lambda x : x[1], points.items()))

print(sum(list(map(lambda x : 1 if x > 1 else 0, overlap))))
