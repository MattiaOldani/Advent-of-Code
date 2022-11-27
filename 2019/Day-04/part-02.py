# Solution: 1306

with open("input.txt", "r") as f:
    range_ = f.readline().strip().split("-")

start = int(range_[0])
end = int(range_[1])

counter = 0
for i in range(start+1, end):
    valid = 0
    number = str(i)
    for t in range(len(number)-1):
        if number[t+1] >= number[t]:
            valid += 1
    
    if valid != 5:
        continue
    
    t = 0
    found = False
    while t < len(number) and not found:
        current = number[t]
        seq = 1
        s = t + 1
        while s < len(number) and number[s] == current:
            seq += 1
            s += 1
        
        if seq == 2:
            found = True
        
        t = s

    counter += (1 if found else 0)

print(counter)
