# Solution: 5329

with open("input.txt", "r") as f:
    rules, updates = [x.split() for x in f.read().split("\n\n")]


rules = [list(map(int, x.split("|"))) for x in rules]
updates = [list(map(int, x.split(","))) for x in updates]

count = 0
for update in updates:
    skip = False
    for a, b in rules:
        if (a in update and b in update) and update.index(a) > update.index(b):
            skip = True
            break

    if not skip:
        count += update[(len(update) - 1) // 2]

print(count)
