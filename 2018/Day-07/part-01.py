# Solution: AHJDBEMNFQUPVXGCTYLWZKSROI

from collections import defaultdict


with open("input.txt", "r") as f:
    data = [x.strip().split(" ") for x in f.readlines()]

graph = defaultdict(lambda: [])

left = set()
right = set()
for line in data:
    graph[line[1]] += [line[0]]
    left.add(line[0])
    right.add(line[1])

starters = sorted(list(left - right))
result = starters.pop(0)

for other in starters:
    graph[other] = []

for n, needed in graph.items():
    if result in needed:
        needed.remove(result)
        graph[n] = needed

nodes = len(left.union(right))
while len(result) < nodes:
    choice = []
    for n, needed in graph.items():
        if len(needed) == 0:
            choice += [n]

    choice.sort()
    choice = choice[0]
    result += choice

    graph.pop(choice)

    for n, needed in graph.items():
        if choice in needed:
            needed.remove(choice)
            graph[n] = needed

print(result)
