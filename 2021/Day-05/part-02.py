# Solution: 17787

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
    else:
        step_y = 1 if y2 > y1 else -1
        step_x = 1 if x2 > x1 else -1
        range_x = range(x1, x2+step_x, step_x)
        range_y = range(y1, y2+step_y, step_y)
        for i in range(len(range_x)):
            try:
                points[(range_x[i],range_y[i])] += 1
            except:
                points[(range_x[i],range_y[i])] = 1
    
overlap = list(map(lambda x : x[1], points.items()))

print(sum(list(map(lambda x : 1 if x > 1 else 0, overlap))))
