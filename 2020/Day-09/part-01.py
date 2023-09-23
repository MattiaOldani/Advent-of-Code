# Solution: 69316178

with open("input.txt", "r") as f:
    numbers = list(map(lambda x : int(x.strip()), f.readlines()))

preamble = [numbers.pop(0) for _ in range(25)]

found = False
while not found:
    current = numbers.pop(0)
    for i in range(len(preamble)-1):
        for j in range(i+1,len(preamble)):
            if preamble[i] + preamble[j] == current:
                found = True
                break
    
    if found:
        found = False
        preamble.pop(0)
        preamble.append(current)
    else:
        print(current)
        break
