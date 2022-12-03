# Solution: 7568

with open("input.txt", "r") as f:
    rucksack = list(map(lambda x : x.strip(), f.readlines()))

counter = 0
for r in rucksack:
    half = int(len(r)/2)
    first = r[:half]
    second = r[half:]
    for item in first:
        if item in second:
            if item.islower():
                counter  += ord(item) - 96
            else:
                counter += ord(item) - 38
            break

print(counter)
