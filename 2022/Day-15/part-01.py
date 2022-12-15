# Solution: 5564017

with open("input.txt", "r") as f:
    maps = list(map(lambda x : x.strip().split(", "), f.readlines()))

END = 2000000

line = dict()
couples = list()
for m in maps:
    sx = int(m[0].split(" ")[2].split("=")[1])
    sy = int(m[1].split(":")[0].split("=")[1])
    if sy == END:
        line[sx] = "S"
    bx = int(m[1].split("x=")[-1])
    by = int(m[2].split("=")[1])
    if by == END:
        line[bx] = "B"
    couples.append([sx,sy,bx,by])

for couple in couples:
    sx,sy,bx,by = couple
    length = abs(sy-by) + abs(sx-bx)
    remain = length - abs(END - sy)

    if remain < 0:
        continue
    
    line[sx] = "#"
    for i in range(1,remain+1):
        if sx+i not in line:
            line[sx+i] = "#"
        if sx-i not in line:
            line[sx-i] = "#"

line = list(filter(lambda x : x[1] == "#", line.items()))

print(len(line))
