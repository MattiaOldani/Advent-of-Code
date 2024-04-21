# Solution: 169

from __future__ import annotations


class Program:
    def __init__(self, number: int) -> None:
        self.number = number
        self.neighbors = []

    def add_neighbor(self, neighbor: Program) -> None:
        self.neighbors.append(neighbor)

    def contains_zero(self, visited: set) -> bool:
        if self.number == 0:
            return True

        if self.number in visited:
            return False

        visited.add(self.number)

        for neighbor in self.neighbors:
            if neighbor.number == 0:
                return True
            
            if neighbor.contains_zero(visited):
                return True
        
        return False


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
for number in numbers:
    if programs[number].contains_zero(set()):
        count += 1

print(count)
