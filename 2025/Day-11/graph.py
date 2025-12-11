with open("input.txt", "r") as f:
    data = [x.strip().replace(":", "").split() for x in f.readlines()]

graph = []
for line in data:
    source = line.pop(0)
    for destination in line:
        graph.append(f"{source} -> {destination}")

for edges in graph:
    print(edges)
