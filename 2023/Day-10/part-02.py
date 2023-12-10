# Solution: 451

from matplotlib.path import Path


def dfs(grid: list[list[str]], start_x: int, start_y: int, movements: dict) -> list[tuple[int]]:
    x_len = len(grid[0]) - 1
    y_len = len(grid) - 1
    
    vertex = [(start_x, start_y)]
    
    distance = 1
    distances = {(start_x, start_y) : 0}
    while True:
        current = grid[start_y][start_x]
        allowed_movements = movements[current]
        
        moved = False
        for movement in allowed_movements:
            x, y, neighbors = movement
            x = x + start_x
            y = y + start_y
            if 0 <= x <= x_len and 0 <= y <= y_len and grid[y][x] in neighbors and (x,y) not in distances:
                start_x = x
                start_y = y
                vertex.append((x,y))
                
                distances[(x,y)] = distance
                distance += 1
                
                current = grid[y][x]
                moved = True
                
                break
        
        if not moved:
            break
    
    return vertex


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip(), f.readlines()))

start_x = 0
start_y = 0
for y,line in enumerate(data):
    if line.find("S") > -1:
        start_x = line.find("S")
        start_y = y
        break

movements = {
    "S" : [(1, 0, "-J7"), (0, 1, "|LJ"), (-1, 0, "-LF"), (0, -1, "|7F")],
    "|" : [(0, 1, "|LJ"), (0, -1, "|7F")],
    "-" : [(1, 0, "-J7"), (-1, 0, "-LF")],
    "L" : [(1, 0, "-J7"), (0, -1, "|7F")],
    "J" : [(-1, 0, "-LF"), (0, -1, "|7F")],
    "7" : [(0, 1, "|LJ"), (-1, 0, "-LF")],
    "F" : [(1, 0, "-J7"), (0, 1, "|LJ")]
}

grid = [list(line) for line in data]
vertex = dfs(grid, start_x, start_y, movements)

path = Path(vertex)

count = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if (x,y) in vertex:
            continue
        if path.contains_point((x,y)):
            count += 1

print(count)
