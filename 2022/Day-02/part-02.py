# Solution: 13187

with open("input.txt", "r") as f:
    rounds = list(map(lambda x : x.strip().split(), f.readlines()))

OUTCOME = {
    "X" : 0,
    "Y" : 3,
    "Z" : 6
}

POINTS = {
    "A" : [3, 1, 2],
    "B" : [1, 2, 3],
    "C" : [2, 3, 1]
}

total = 0
for round in rounds:
    opponent = round[0]
    mine = round[1]
    outcome = OUTCOME[mine]
    total += (outcome + POINTS[opponent][int(outcome/3)])

print(total)
