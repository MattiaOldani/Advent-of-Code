# Solution: 520

import networkx as nx


with open("input.txt", "r") as f:
    data = [x.strip().split(")") for x in f.readlines()]


graph = nx.Graph()
for p1, p2 in data:
    graph.add_nodes_from([p1, p2])
    graph.add_edge(p1, p2)

print(nx.shortest_path_length(graph, "YOU", "SAN") - 2)
