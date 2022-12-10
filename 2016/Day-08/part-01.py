# Solution: 106

with open("input.txt", "r") as f:
    commands = list(map(lambda x : x.strip().split(" "), f.readlines()))

up = 0
screen = [[0 for i in range(50)] for j in range(6)]

for command in commands:
    match command:
        case ["rect", *other]:
            wide,tall = list(map(int, other))
            for i in range(tall):
                for j in range(wide):
                    screen[i][j] = 1
        case [where, *other]:
            selected,shift = list(map(int, other))
            
            if where == "row":
                row = screen[selected]
            else:
                row = [screen[i][selected] for i in range(len(screen))]
            
            for i in range(shift):
                last = row.pop()
                row.insert(0, last)

            if where == "column":
                for i in range(len(screen)):
                    screen[i][selected] = row[i]
    
for row in screen:
    up += sum(row)

print(up)
