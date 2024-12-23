# Solution: cl,ei,fd,hc,ib,kq,kv,ky,rv,vf,wk,yx,zf

import networkx as nx


with open("input.txt", "r") as f:
    edges = [x.strip().split("-") for x in f.readlines()]


graph = nx.Graph()
graph.add_edges_from(edges)

for _, d in graph.nodes(data=True):
    d["weight"] = 1

max_clique = nx.max_weight_clique(graph)[0]

print(",".join(sorted(max_clique)))
