# Solution: 1101

from heapq import heappop, heappush


with open("input.txt", "r") as f:
    grid = list(map(lambda x : [int(y) for y in x.strip()], f.readlines()))

visited = set()

queue = [(0, 0, 0, 0, 0, 0)]
while len(queue) > 0:
    heat, i, j, i_direction, j_direction, steps = heappop(queue)

    if i == len(grid)-1 and j == len(grid[i])-1 and steps >= 4:
        print(heat)
        break

    if (i, j, i_direction, j_direction, steps) in visited:
        continue

    visited.add((i, j, i_direction, j_direction, steps))

    if (i_direction,j_direction) == (0,0):
        heappush(queue, (grid[0][1], 0, 1, 0, 1, 1))
        heappush(queue, (grid[1][0], 1, 0, 1, 0, 1))
        continue

    if steps < 10 and 0 <= i+i_direction < len(grid) and 0 <= j+j_direction < len(grid[i]):
        new_i = i + i_direction
        new_j = j + j_direction
        heappush(queue, (heat + grid[new_i][new_j], new_i, new_j, i_direction, j_direction, steps+1))

    if steps >= 4:
        for new_i_direction,new_j_direction in [(0,1), (1,0), (0, -1), (-1,0)]:
            if (i_direction,j_direction) != (new_i_direction,new_j_direction) and (i_direction,j_direction) != (-new_i_direction,-new_j_direction):
                if 0 <= i+new_i_direction < len(grid) and 0 <= j+new_j_direction < len(grid[i]):
                    new_i = i + new_i_direction
                    new_j = j + new_j_direction
                    heappush(queue, (heat + grid[new_i][new_j], new_i, new_j, new_i_direction, new_j_direction, 1))
