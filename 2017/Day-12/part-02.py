# Solution: 179

from __future__ import annotations


class Program:
    def __init__(self, number: int) -> None:
        self.number = number
        self.neighbors = []

    def add_neighbor(self, neighbor: Program) -> None:
        self.neighbors.append(neighbor)

    def get_groups(self, remove: set, visited: set) -> None:
        if self.number in visited:
            return

        remove.add(self.number)
        visited.add(self.number)

        for neighbor in self.neighbors:
            neighbor.get_groups(remove, visited)


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" <-> "), f.readlines()))

numbers = set()
programs = dict()
for line in data:
    start,ends = int(line[0]), [int(l) for l in line[1].split()]
    
    numbers.add(start)
    programs[start] = Program(start)

    for end in ends:
        numbers.add(end)
        programs[end] = Program(end)

for line in data:
    start,ends = int(line[0]), [int(l) for l in line[1].split()]
    
    current = programs[start]
    for end in ends:
        current.add_neighbor(programs[end])

count = 0
while len(numbers) > 0:
    number = numbers.pop()
    
    remove = set()
    programs[number].get_groups(remove, set())

    numbers = numbers.difference(remove)
    
    count += 1

print(count)
