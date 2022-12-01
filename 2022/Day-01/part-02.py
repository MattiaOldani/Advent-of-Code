# Solution: 199628

with open("input.txt", "r") as f:
    calories = list(map(lambda x : x.strip(), f.readlines()))

calories.append("")

total = 0
elves = list()
for c in calories:
    if c == "":
        elves.append(total)
        total = 0
    else:
        total += int(c)

elves.append(total)
elves.sort(reverse=True)

print(sum(elves[0:3]))
