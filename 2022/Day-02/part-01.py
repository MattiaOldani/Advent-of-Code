# Solution: 11449

with open("input.txt", "r") as f:
    rounds = list(map(lambda x : x.strip().split(), f.readlines()))

POINTS = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

OUTCOME = {
    "A" : [3, 6, 0],
    "B" : [0, 3, 6],
    "C" : [6, 0, 3]
}

total = 0
for round in rounds:
    opponent = round[0]
    mine = round[1]
    point = POINTS[mine]
    total += (point + OUTCOME[opponent][point-1])

print(total)
