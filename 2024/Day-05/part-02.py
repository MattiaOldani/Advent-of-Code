# Solution: 5833


def update_respect_rules(update, rules) -> bool:
    for a, b in rules:
        if (a in update and b in update) and update.index(a) > update.index(b):
            return False

    return True


with open("input.txt", "r") as f:
    rules, updates = [x.split() for x in f.read().split("\n\n")]


rules = [list(map(int, x.split("|"))) for x in rules]
updates = [list(map(int, x.split(","))) for x in updates]

count = 0
for update in updates:
    if update_respect_rules(update, rules):
        continue

    rules_to_check = []
    for a, b in rules:
        if a in update and b in update:
            rules_to_check += [(a, b)]

    while True:
        for a, b in rules_to_check:
            ia = update.index(a)
            ib = update.index(b)
            if ia > ib:
                update[ia], update[ib] = update[ib], update[ia]
                break

        if update_respect_rules(update, rules_to_check):
            count += update[(len(update) - 1) // 2]
            break

print(count)
