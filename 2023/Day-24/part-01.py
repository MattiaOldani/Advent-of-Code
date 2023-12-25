# Solution: 20434

from __future__ import annotations
from math import sqrt


class _2DPoint:
    START = 200000000000000
    END = 400000000000000

    def __init__(self, coordinates: tuple, velocity: tuple) -> None:
        self.coordinates = coordinates
        self.velocity = velocity

    def get_line_parameter(self) -> tuple:
        fx,fy = self.coordinates
        sx,sy = fx+self.velocity[0], fy+self.velocity[1]
        
        m = (sy - fy) / (sx - fx)
        q = fy - m*fx
        
        return (m,q)

    def check_intersection(self, other: _2DPoint) -> bool:
        cm,cq = self.get_line_parameter()
        om,oq = other.get_line_parameter()

        if cm == om:
            return False

        x = (oq - cq) / (cm - om)
        y = cm * x + cq

        cx,cy = self.coordinates
        ncx = cx + self.velocity[0]
        ncy = cy + self.velocity[1]

        ox,oy = other.coordinates
        nox = ox + other.velocity[0]
        noy = oy + other.velocity[1]

        cd = sqrt((x - cx)**2 + (y - cy)**2)
        ncd = sqrt((x - ncx)**2 + (y - ncy)**2)

        od = sqrt((x - ox)**2 + (y - oy)**2)
        nod = sqrt((x - nox)**2 + (y - noy)**2)

        return _2DPoint.START <= x <= _2DPoint.END and _2DPoint.START <= y <= _2DPoint.END and ncd < cd and nod < od


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" @ "), f.readlines()))

points = []
for line in data:
    x,y,_ = [int(l) for l in line[0].split()]
    vx,vy,_ = [int(l) for l in line[1].split()]

    point = _2DPoint((x,y), (vx,vy))
    points.append(point)

count = 0
for i,point in enumerate(points):
    for other in points[i+1:]:
        if point.check_intersection(other):
            count += 1

print(count)
