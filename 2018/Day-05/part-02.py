# Solution: 5774

with open("input.txt", "r") as f:
    polymers = f.readline().strip()

elements = list()
for p in polymers:
    if p.lower() not in elements:
        elements.append(p.lower())

scores = list()
for element in elements:
    current = str(polymers).replace(element, "")
    current = current.replace(element.upper(), "")

    i = 0
    while i < len(current):
        p1 = current[i]
        p2 = current[i-1]
            
        if (p1.isupper() and p1.lower() == p2) or (p1.islower() and p1.upper() == p2):
            current = current.replace(p2+p1, "", 1)
            i -= 1
            if i == 0:
                i = 1
        else:
            i += 1

    scores.append(len(current))

print(min(scores))
