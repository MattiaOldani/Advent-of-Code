# Solution: 4550283

def extract(binary, change):
    i = 0
    while len(binary) > 1:
        column = [binary[t][i] for t in range(len(binary))]
        found = 1 if column.count('1') >= column.count('0') else 0
        found = (found + change) % 2
        binary = list(filter(lambda x : x[i] == str(found), binary))
        i += 1
    
    res,p = 0,len(binary[0])-1
    for c in binary[0]:
        res += int(c) * 2**p
        p -= 1
    return res


with open("input.txt", "r") as f:
    binary = list(map(lambda x : x.strip(), f.readlines()))

odue = extract(binary.copy(), 0)
codue = extract(binary.copy(), 1)

print(odue * codue)
