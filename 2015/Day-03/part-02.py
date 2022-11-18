# Solution: 2639

def move(m, x, y):
    match m:
        case '^': y += 1
        case 'v': y -= 1
        case '>': x += 1 
        case '<': x -= 1
    return (x,y)


with open('input.txt', 'r') as f:
    movements = f.readline()
    xs = 0
    ys = 0
    xr = 0
    yr = 0
    turn = 0
    counter = 1
    visited = [(0,0)]
    for m in movements:
        if turn == 0:
            xs, ys = move(m, xs, ys)
            current = (xs,ys)
        else:
            xr, yr = move(m, xr, yr)
            current = (xr,yr)
        if current not in visited:
            counter += 1
            visited.append(current)
        turn = 1 - turn
    print(counter)
