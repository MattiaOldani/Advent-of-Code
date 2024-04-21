# Solution: 1469

with open("input.txt", "r") as f:
    moves = f.readline().strip().split(",")

x,y = 0,0

max_distance = 0
for move in moves:
    match move:
        case "n":
            y += 1
        case "ne":
            x += 1
            y += 1
        case "se":
            x += 1
            y -= 1
        case "s":
            y -= 1
        case "sw":
            x -= 1
            y -= 1
        case "nw":
            x -= 1
            y += 1
    
    max_distance = max(max_distance, max(abs(x), abs(y)))

print(max_distance)
