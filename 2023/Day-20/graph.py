with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" -> "), f.readlines()))

sources, destinations = [d[0] for d in data], [d[1].split() for d in data]

graph = []
for start,ends in zip(sources,destinations):
    for end in ends:
        graph.append(f"{start.removeprefix('%').removeprefix('&')} -> {end};")

for edges in sorted(graph):
    print(edges)
