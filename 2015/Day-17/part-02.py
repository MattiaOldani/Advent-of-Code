# Solution: 18

from itertools import combinations


with open("input.txt", "r") as f:
    capacities = list(map(lambda x : int(x.strip()), f.readlines()))

capacities.sort()

count = dict()
for i in range(1, len(capacities)+1):
    count[i] = 0
    combinations_to_check = list(combinations(capacities, i))
    for combination in combinations_to_check:
        count[i] += 1 if sum(combination) == 150 else 0

for i in range(1, len(capacities)+1):
    if count[i] > 0:
        print(count[i])
        break
