# Solution: 49710

with open("input.txt", "r") as f:
    games = list(map(lambda x : x.strip().split(" "), f.readlines()))

count = 0
for game in games:
    id_ = int(game.pop(0))
    red = 0
    green = 0
    blue = 0

    for i in range(0, len(game), 2):
        quantity = int(game[i])
        color = game[i+1]
        
        match [color, quantity]:
            case ["red", n]:
                red = max(red, n)
            case ["green", n]:
                green = max(green, n)
            case ["blue", n]:
                blue = max(blue, n)
    
    count += (red * green * blue)

print(count) 
