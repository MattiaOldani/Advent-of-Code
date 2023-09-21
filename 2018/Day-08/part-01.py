# Solution: 48260

from __future__ import annotations


class Node:
    def __init__(self) -> None:
        self.child: list[Node] = list()
        self.meta: list[int] = list()
    
    def add_child(self, child: Node) -> None:
        self.child.append(child)

    def add_meta(self, meta: int) -> None:
        self.meta.append(meta)
    
    def get_tree_meta(self) -> int:
        return sum(self.meta) + sum([c.get_tree_meta() for c in self.child])


def create_tree(data: list[int]) -> Node:
    n_child = data.pop(0)
    n_meta = data.pop(0)
    
    root = Node()
    
    for _ in range(n_child):
        root.add_child(create_tree(data))
    
    for _ in range(n_meta):
        root.add_meta(data.pop(0))
    
    return root


with open("input.txt", "r") as f:
    data = list(map(int, f.read().strip().split(" ")))

tree = create_tree(data)

print(tree.get_tree_meta())
