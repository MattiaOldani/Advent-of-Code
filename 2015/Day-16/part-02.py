# Solution: 241

with open("input.txt", "r") as f:
    aunts = list(map(lambda x : x.strip().split(" "), f.readlines()))

GOAL = {
    "children": lambda x: x == 3,
    "cats": lambda x : x > 7,
    "samoyeds": lambda x : x == 2,
    "pomeranians": lambda x : x < 3,
    "akitas": lambda x : x == 0,
    "vizslas": lambda x : x == 0,
    "goldfish": lambda x : x < 5,
    "trees": lambda x : x > 3,
    "cars": lambda x : x == 2,
    "perfumes": lambda x : x == 1
}

for sue in aunts:
    check = 0
    for i in range(2, len(sue), 2):
        key = sue[i].removesuffix(":")
        value = int(sue[i+1].removesuffix(","))
        check += 1 if GOAL[key](value) else 0
    if check == (len(sue) - 2) / 2:
        print(int(sue[1].removesuffix(":")))
        break
