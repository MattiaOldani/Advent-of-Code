# Solution: 10496

with open("input.txt", "r") as f:
    polymers = f.readline().strip()

i = 1
while i < len(polymers):
    p1 = polymers[i]
    p2 = polymers[i-1]
        
    if (p1.isupper() and p1.lower() == p2) or (p1.islower() and p1.upper() == p2):
        polymers = polymers.replace(p2+p1, "", 1)
        i -= 1
        if i == 0:
            i = 1
    else:
        i += 1

print(len(polymers))
