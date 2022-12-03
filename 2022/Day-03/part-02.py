# Solution: 2780

with open("input.txt", "r") as f:
    rucksack = list(map(lambda x : x.strip(), f.readlines()))

counter = 0
for i in range(0,len(rucksack),3):
    r = rucksack[i:i+3]
    for item in r[0]:
        if item in r[1] and item in r[2]:
            if item.islower():
                counter  += ord(item) - 96
            else:
                counter += ord(item) - 38
            break

print(counter)
