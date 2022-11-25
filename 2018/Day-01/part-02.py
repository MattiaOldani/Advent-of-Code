# Solution: 76787

with open("input.txt", "r") as f:
    freq = f.readlines()
    
freq = list(map(lambda x : int(x.strip()), freq))

i = 0
sum = 0
visited = [0]
while True:
    sum += freq[i]
    if sum in visited:
        print(sum)
        break

    i = (i + 1) % len(freq)
    visited.append(sum)
