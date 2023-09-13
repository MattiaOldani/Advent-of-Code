# Solution: 1304

from itertools import combinations


with open("input.txt", "r") as f:
    capacities = list(map(lambda x : int(x.strip()), f.readlines()))

capacities.sort()

count = 0
for i in range(1, len(capacities)+1):
    combinations_to_check = list(combinations(capacities, i))
    if i < 4:
        print(combinations_to_check)
    for combination in combinations_to_check:
        count += 1 if sum(combination) == 150 else 0

print(count)
