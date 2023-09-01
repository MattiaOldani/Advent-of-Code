# Solution: 618

from itertools import permutations


def evaluate(table, happiness):
    count = 0
    table_len = len(table)
    for i in range(table_len):
        current = table[i]
        right = table[(i+1) % table_len]
        left = table[(i-1+table_len) % table_len]
        count += happiness[current][right]
        count += happiness[current][left]
    return count


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" "), f.readlines()))

friends = set()
happiness = dict()
for line in data:
    name = line[0]
    value = int(line[2]) if line[1] == "gain" else -int(line[2])
    other = line[3]
    friends.add(line[0])
    if name not in happiness:
        happiness[name] = dict()
    happiness[name][other] = value

best = 0
for table in permutations(friends):
    best = max(best, evaluate(table, happiness))

print(best)
