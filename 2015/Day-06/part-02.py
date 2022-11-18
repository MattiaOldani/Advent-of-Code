# Solution: 15343601

def toggle(field, cmd, op):
    start_x, start_y = list(map(lambda x : int(x), cmd[0].split(",")))
    end_x, end_y = list(map(lambda x : int(x), cmd[2].split(",")))

    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            match op:
                case "on": field[i][j] += 1
                case "off": field[i][j] -= 1
                case "toggle": field[i][j] += 2
            if field[i][j] < 0:
                field[i][j] = 0


with open("input.txt", "r") as f:
    commands = f.readlines()

    field = [[0 for i in range(1000)] for j in range(1000)]

    for cmd in commands:
        cmd = cmd.split(" ")
        toggle(field, cmd[1:], cmd[0])
        
    print(sum([sum(i) for i in field]))
