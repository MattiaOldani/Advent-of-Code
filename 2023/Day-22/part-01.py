# Solution: 428

from __future__ import annotations


class Brick:
    def __init__(self, id_: int, x: tuple, y: tuple, z: tuple) -> None:
        self.id_ = id_
        self.x = x
        self.y = y
        self.z = z
        self.lowest = min(z)
        self.base = []

    def move_down(self, step: int) -> Brick:
        return Brick(self.id_, self.x, self.y, (self.z[0]-step, self.z[1]-step))

    def can_move_down(self) -> bool:
        return self.lowest > 1

    def intersection(self, other) -> bool:
        current = set(
            [(x,y,z) for x in range(min(self.x), max(self.x)+1)
                     for y in range(min(self.y), max(self.y)+1)
                     for z in range(min(self.z), max(self.z)+1)
            ]
        )

        other = set(
            [(x,y,z) for x in range(min(other.x), max(other.x)+1)
                     for y in range(min(other.y), max(other.y)+1)
                     for z in range(min(other.z), max(other.z)+1)
            ]
        )

        return len(current.intersection(other)) > 0

    def xy_intersection(self, other) -> bool:
        current = set(
            [(x,y) for x in range(min(self.x), max(self.x)+1)
                   for y in range(min(self.y), max(self.y)+1)
            ]
        )

        other = set(
            [(x,y) for x in range(min(other.x), max(other.x)+1)
                   for y in range(min(other.y), max(other.y)+1)
            ]
        )

        return len(current.intersection(other)) > 0

    def add_base(self, id_: int) -> None:
        self.base.append(id_)

    def fall(self, id_: int) -> bool:
        return id_ in self.base and len(self.base) == 1


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip(), f.readlines()))

bricks = list()
for i,line in enumerate(data):
    start,end = line.split(" ~ ")
    
    sx,sy,sz = [int(s) for s in start.split()]
    ex,ey,ez = [int(s) for s in end.split()]

    bricks.append(Brick(i, (sx,ex), (sy,ey), (sz,ez)))

bricks.sort(key=lambda b: b.lowest)

for i,brick in enumerate(bricks):
    if not brick.can_move_down():
        continue
    
    bricks_under_current = [b for b in bricks[:i] if b.xy_intersection(brick)]
    if len(bricks_under_current) == 0:
        step = min(brick.z) - 1
    else:
        step = min(brick.z) - max([max(b.z) for b in bricks_under_current]) - 1

    moved_down = brick.move_down(step)
    
    check_intersections = brick.move_down(step+1)    
    for j,other in enumerate(bricks):
        if i <= j:
            break

        if check_intersections.intersection(other):
            moved_down.add_base(j)
    
    bricks[i] = moved_down

count = 0
for i in range(len(bricks)):
    remove = True
    for j,other in enumerate(bricks):
        if i == j:
            continue
        
        if other.fall(i):
            remove = False
            break
    
    if remove:
        count += 1

print(count)
