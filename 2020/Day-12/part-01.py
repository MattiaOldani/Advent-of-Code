# Solution: 582

with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip(), f.readlines()))

index_directions = 0
directions = [[1,0], [0,-1], [-1,0], [0,1]]
current_direction = directions[index_directions]

x,y = 0,0
for line in data:
    command = line[0]
    value = int(line[1:])
    match command:
        case "N": y += value
        case "S": y -= value
        case "E": x += value
        case "W": x -= value
        case "L":
            index_directions = ((index_directions - value // 90) % 4 + 4) % 4
            current_direction = directions[index_directions]
        case "R":
            index_directions = (index_directions + value // 90) % 4
            current_direction = directions[index_directions]
        case "F":
            x += current_direction[0] * value
            y += current_direction[1] * value

print(abs(x) + abs(y))
