# Solution: 1031

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
for i in range(len(starters)):
    starters[i] = [starters[i], 60 + ord(starters[i]) - ord("A") + 1]

time = 0
result = ""

nodes = len(left.union(right))
while len(result) < nodes:
    workers = min(5, len(starters))

    index = 0
    for _ in range(workers):
        starters[index][1] -= 1
        if starters[index][1] == 0:
            result += starters[index][0]
            starters.pop(index)

            for n, needed in graph.items():
                if result[-1] in needed:
                    needed.remove(result[-1])
                    graph[n] = needed
        else:
            index += 1

    new = []
    for n, needed in graph.items():
        if len(needed) == 0:
            new += [[n, 60 + ord(n) - ord("A") + 1]]

    starters += new

    for r in new:
        graph.pop(r[0])

    time += 1

print(time)
