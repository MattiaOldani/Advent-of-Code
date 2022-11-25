# Solution: 5880

with open("input.txt", "r") as f:
    rows = f.readlines()

two = 0
three = 0
for row in rows:
    char = [r for r in row]
    char.sort()

    occ = dict()
    for c in char:
        try:
            occ[c] += 1
        except:
            occ[c] = 1
    
    otw,oth = False,False
    for k in occ.items():
        if k[1] == 2 and not otw:
            two += 1
            otw = True
        if k[1] == 3 and not oth:
            three += 1
            oth = True
    
print(two * three)
