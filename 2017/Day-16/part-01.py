# Solution: fgmobeaijhdpkcln

with open("input.txt", "r") as f:
    moves = f.readline().strip().split(",")

programs = [chr(i) for i in range(97,113)]

for move in moves:
    match move[0]:
        case "s":
            n = int(move[1:])
            while n > 0:
                programs.insert(0, programs.pop())
                n -= 1
        case "x":
            p1 = int(move[1:].split("/")[0])
            p2 = int(move[1:].split("/")[1])
            programs[p1],programs[p2] = programs[p2],programs[p1]
        case "p":
            p1 = programs.index(move[1:].split("/")[0])
            p2 = programs.index(move[1:].split("/")[1])
            programs[p1],programs[p2] = programs[p2],programs[p1]

print("".join(programs))
