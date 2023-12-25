# Solution: 547080

import networkx as nx


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(), f.readlines()))

graph = nx.Graph({line[0]: line[1:] for line in data})

edges = nx.minimum_edge_cut(graph)
assert len(edges) == 3

graph.remove_edges_from(edges)
groups = list(nx.connected_components(graph))
assert len(groups) == 2

print(len(groups[0]) * len(groups[1]))
