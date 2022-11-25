# Solution: 105231

with open("input.txt", "r") as f:
    squares = list(map(lambda x : x.strip(), f.readlines()))

grid = [[0 for i in range(1000)] for j in range(1000)]

for square in squares:
    square = list(map(lambda x : int(x), square.split(" ")))
    j = square[1]
    i = square[2]
    dj = square[3]
    di = square[4]
    for t in range(i,i+di):
        for s in range(j,j+dj):
            grid[t][s] += 1

counter = 0
for row in grid:
    for col in row:
        if col > 1:
            counter += 1

print(counter)
