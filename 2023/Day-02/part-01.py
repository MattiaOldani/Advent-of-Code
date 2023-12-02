# Solution: 2683

with open("input.txt", "r") as f:
    games = list(map(lambda x : x.strip().split(" "), f.readlines()))

RED = 12
GREEN = 13
BLUE = 14

count = 0
for game in games:
    id_ = int(game.pop(0))

    possible = True
    for i in range(0, len(game), 2):
        quantity = int(game[i])
        color = game[i+1].upper()

        possible = possible and eval(f"quantity <= {color}")
        if not possible:
            break
    
    if possible:
        count += id_

print(count) 
