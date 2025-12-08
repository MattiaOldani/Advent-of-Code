# Solution: 6083499488

import heapq
from math import sqrt


class Point:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z

    def __eq__(self, value) -> bool:
        if not isinstance(value, Point):
            return False

        return self.X == value.X and self.Y == value.Y and self.Z == value.Z

    def distance(self, point) -> float:
        return sqrt(
            (self.X - point.X) ** 2 + (self.Y - point.Y) ** 2 + (self.Z - point.Z) ** 2
        )

    def __hash__(self) -> int:
        return hash((self.X, self.Y, self.Z))


with open("input.txt", "r") as f:
    data = [list(map(int, x.strip().split(","))) for x in f.readlines()]

points = []
for line in data:
    points += [Point(*line)]

distance = []
for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        current_distance = points[i].distance(points[j])
        heapq.heappush(distance, (current_distance, points[i], points[j]))

circuits = []
connected = set()
while True:
    d, p1, p2 = heapq.heappop(distance)

    connected.add(p1)
    connected.add(p2)

    indexes = []

    same_circuit = False
    for i, circuit in enumerate(circuits):
        if p1 in circuit and p2 in circuit:
            same_circuit = True
            break
        elif p1 in circuit or p2 in circuit:
            circuit.add(p1)
            circuit.add(p2)
            indexes += [i]

    if same_circuit:
        continue

    if len(indexes) == 0:
        circuits += [set([p1, p2])]
        continue

    merged = set()
    new_circuits = []
    for i, circuit in enumerate(circuits):
        if i in indexes:
            merged = merged.union(circuit)
        else:
            new_circuits += [circuit]

    new_circuits += [merged]
    circuits = new_circuits

    if len(circuits) == 1 and len(connected) == len(points):
        print(p1.X * p2.X)
        break
