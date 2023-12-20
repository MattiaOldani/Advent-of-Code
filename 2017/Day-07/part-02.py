# Solution: 420

from __future__ import annotations
from sys import exit


class Disc:
    def __init__(self, weight: int) -> None:
        self.weight = weight
        self.sub = []

    def add_sub_disc(self, other: Disc) -> None:
        self.sub.append(other)

    def balance(self) -> int:
        if len(self.sub) == 0:
            return self.weight

        weights = []
        for sub in self.sub:
            weights.append(sub.balance())

        no_repetitions = set(weights)
        if len(no_repetitions) == 1:
            return self.weight + sum(weights)

        different = [w for w in no_repetitions if weights.count(w) == 1][0]        
        index = weights.index(different)
        
        start = self.sub[index].weight

        print(start + (weights[index-1] -  weights[index])) 
        exit(0)


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(), f.readlines()))

discs = dict()
for line in data:
    name = line[0]
    weight = int(line[1])
    discs[name] = Disc(weight)

for line in data:
    if len(line[2:]) > 0:
        name = line[0]
        current = discs[name]
        for other in line[2:]:
            discs[name].add_sub_disc(discs[other])

start = discs["eugwuhl"]

start.balance()
