# Solution: 11558423398893

with open("input.txt", "r") as f:
    maps = list(map(lambda x : x.strip().split(", "), f.readlines()))

couples = list()
for m in maps:
    sx = int(m[0].split(" ")[2].split("=")[1])
    sy = int(m[1].split(":")[0].split("=")[1])
    bx = int(m[1].split("x=")[-1])
    by = int(m[2].split("=")[1])
    couples.append([sx,sy,bx,by])

for y in range(4000001):
    all_ranges = list()
    for couple in couples:
        sx,sy,bx,by = couple
        length = abs(sy-by) + abs(sx-bx)
        remain = length - abs(sy - y)
        
        if remain < 0:
            continue
        
        all_ranges.append([sx - remain, sx + remain])
    
    all_ranges.sort(key=lambda x : x[0])
    
    remain = list()
    for i in range(1,len(all_ranges)):
        first = all_ranges[i-1]
        second = all_ranges[i]

        if second[0] <= first[1] <= second[1] or first[1] + 1 == second[0]:
            all_ranges[i] = [first[0], second[1]]
        elif first[0] <= second[0] and first[1] >= second[1]:
            all_ranges[i] = first   
        else:
            remain.append(first)
    
    remain.append(all_ranges[-1])
    
    if len(remain) > 1:
        print(4000000 * (remain[0][1] + 1) + y)
        break
