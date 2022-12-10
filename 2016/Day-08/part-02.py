# Solution: CFLELOYFCS

with open("input.txt", "r") as f:
    commands = list(map(lambda x : x.strip().split(" "), f.readlines()))

up = 0
screen = [["." for i in range(50)] for j in range(6)]

for command in commands:
    match command:
        case ["rect", *other]:
            wide,tall = list(map(int, other))
            for i in range(tall):
                for j in range(wide):
                    screen[i][j] = "#"
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
    
message = str()
for row in screen:
    message = message + ''.join(row) + "\n"

print(message)

print(message.replace(".", " ").rstrip())
