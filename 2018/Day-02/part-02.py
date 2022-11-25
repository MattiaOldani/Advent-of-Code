# Solution: tiwcdpbseqhxryfmgkvjujvza

with open("input.txt", "r") as f:
    rows = f.readlines()

for i in range(len(rows)-1):
    found = False
    for j in range(i+1, len(rows)):
        r1 = rows[i]
        r2 = rows[j]
        diff = 0

        res = str()
        for t in range(len(r1)):
            if r1[t] != r2[t]:
                diff += 1
            else:
                res += r1[t]

        if diff == 1:
            print(res)
            found = True
            break
