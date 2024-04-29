# Solution: lgmkacfjbopednhi

from collections import defaultdict


with open("input.txt", "r") as f:
    moves = f.readline().strip().split(",")

programs = [chr(i) for i in range(97,113)]

seen = defaultdict(lambda: [])
seen["".join(programs)].append(0)

i = 1
loop = False
while i <= 1000000000:
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
    
    seen["".join(programs)].append(i)

    if not loop and len(list(filter(lambda x: len(x) > 1, seen.values()))) == 1:
        start,end = list(filter(lambda x: len(x) > 1, seen.values()))[0]
        range_ = end - start
        step = (1000000000 - i) // range_
        i = i + step * range_
        loop = True

    i += 1

print("".join(programs))
