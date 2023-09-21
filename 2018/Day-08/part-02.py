# Solution: 25981

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
        if len(self.child) == 0:
            return sum(self.meta)
        
        root_meta = 0
        for meta in self.meta:
            if meta >= 1 and meta <= len(self.child):
                root_meta += self.child[meta - 1].get_tree_meta()
        
        return root_meta


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
