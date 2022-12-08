# Solution: 10496

with open("input.txt", "r") as f:
    polymers = f.readline().strip()

while True:
    couple = False
    for i in range(1,len(polymers)):
        p1 = polymers[i]
        p2 = polymers[i-1]
        
        if (p1.isupper() and p1.lower() == p2) or (p1.islower() and p1.upper() == p2):
            couple = True
            polymers = polymers.replace(p2+p1, "", 1)
            break
    
    if couple:
        continue

    break

print(len(polymers))
