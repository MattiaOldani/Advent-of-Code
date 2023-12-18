# Solution: 7434

import sys
sys.setrecursionlimit(10000)


def explore(grid: list[list[str]], i: int, j: int, direction: str, visited: dict) -> None:
    if not 0 <= i <= len(grid)-1 or not 0 <= j <= len(grid[0])-1:
        return

    if (i,j,direction) in visited:
        return
    
    visited[(i,j,direction)] = True

    match direction:
        case "R":
            match grid[i][j]:
                case "-" | ".":
                    explore(grid, i, j+1, "R", visited)
                case "|":
                    explore(grid, i-1, j, "U", visited)
                    explore(grid, i+1, j, "D", visited)
                case "\\":
                    explore(grid, i+1, j, "D", visited)
                case "/":
                    explore(grid, i-1, j, "U", visited)
        case "L":
            match grid[i][j]:
                case "-" | ".":
                    explore(grid, i, j-1, "L", visited)
                case "|":
                    explore(grid, i-1, j, "U", visited)
                    explore(grid, i+1, j, "D", visited)
                case "\\":
                    explore(grid, i-1, j, "U", visited)
                case "/":
                    explore(grid, i+1, j, "D", visited)
        case "U":
            match grid[i][j]:
                case "|" | ".":
                    explore(grid, i-1, j, "U", visited)
                case "-":
                    explore(grid, i, j-1, "L", visited)
                    explore(grid, i, j+1, "R", visited)
                case "\\":
                    explore(grid, i, j-1, "L", visited)
                case "/":
                    explore(grid, i, j+1, "R", visited)
        case "D":
            match grid[i][j]:
                case "|" | ".":
                    explore(grid, i+1, j, "D", visited)
                case "-":
                    explore(grid, i, j-1, "L", visited)
                    explore(grid, i, j+1, "R", visited)
                case "\\":
                    explore(grid, i, j+1, "R", visited)
                case "/":
                    explore(grid, i, j-1, "L", visited)

    return


with open("input.txt", "r") as f:
    grid = list(map(lambda x : list(x.strip()), f.readlines()))

visited = dict()
explore(grid, 0, 0, "R", visited)

print(len(set([(p[0],p[1]) for p in visited.keys()])))
