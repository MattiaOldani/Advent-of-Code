# Solution: 164

with open("input.txt", "r") as f:
    squares = list(map(lambda x : x.strip(), f.readlines()))

grid = [[0 for i in range(1000)] for j in range(1000)]

visited = list()
for square in squares:
    square = list(map(lambda x : int(x), square.split(" ")))
    box_id = square[0]
    j = square[1]
    i = square[2]
    dj = square[3]
    di = square[4]

    on = False
    for t in range(i,i+di):
        for s in range(j,j+dj):
            if grid[t][s] == 0:
                grid[t][s] = box_id
            else:
                try:
                    visited.remove(grid[t][s])
                except:
                    pass
                on = True

    if not on:
        visited.append(box_id)

print(visited[0])
