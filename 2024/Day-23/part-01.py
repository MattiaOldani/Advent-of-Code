# Solution: 1358

import networkx as nx


with open("input.txt", "r") as f:
    edges = [x.strip().split("-") for x in f.readlines()]


graph = nx.Graph()
graph.add_edges_from(edges)

count = 0
for clique in filter(lambda c: len(c) == 3, nx.enumerate_all_cliques(graph)):
    for node in clique:
        if node.startswith("t"):
            count += 1
            break

print(count)
