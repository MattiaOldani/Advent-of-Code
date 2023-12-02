# Solution: 52069

with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip(), f.readlines()))

rotations = [[1,0], [0,1], [-1,0], [0,-1]]

x, y = 0, 0
wx, wy = 10, 1
for line in data:
    command = line[0]
    value = int(line[1:])
    match command:
        case "N": wy += value
        case "S": wy -= value
        case "E": wx += value
        case "W": wx -= value
        case "L":
            cos, sin = rotations[(value % 360) // 90]
            wx, wy = cos*wx - sin*wy, sin*wx + cos*wy
        case "R":
            cos, sin = rotations[(4 - (value % 360) // 90) % 4]
            wx, wy = cos*wx - sin*wy, sin*wx + cos*wy
        case "F":
            x += wx * value
            y += wy * value

print(abs(x) + abs(y))
