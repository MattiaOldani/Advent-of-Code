# Solution: 40

with open("input.txt", "r") as f:
    aunts = list(map(lambda x : x.strip().split(" "), f.readlines()))

GOAL = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

for sue in aunts:
    check = 0
    for i in range(2, len(sue), 2):
        key = sue[i].removesuffix(":")
        value = int(sue[i+1].removesuffix(","))
        check += 1 if GOAL[key] == value else 0
    if check == (len(sue) - 2) / 2:
        print(int(sue[1].removesuffix(":")))
        break
