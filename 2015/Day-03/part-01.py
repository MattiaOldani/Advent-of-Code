# Solution: 2565

with open('input.txt', 'r') as f:
    movements = f.readline()
    x = 0
    y = 0
    counter = 1
    visited = [(0,0)]
    for m in movements:
        match m:
            case '^': y += 1
            case 'v': y -= 1
            case '>': x += 1
            case '<': x -= 1
        if (x,y) not in visited:
            counter += 1
            visited.append((x,y))
    print(counter)
