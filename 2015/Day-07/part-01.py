# Solution: 46065

with open("input.txt", "r") as f:
    operations = list(map(lambda x : x.strip().split(" -> "), f.readlines()))

i = 0
variables = dict()
while len(operations) > 0:
    src = operations[i % len(operations)][0].split(" ")
    dst = operations[i % len(operations)][1]
    i += 1

    match src:
        case [s1]:
            if s1 in variables.keys():
                src = variables[s1]
            else:
                try:
                    src = int(s1)
                except:
                    continue
        case ["NOT", s1]:
            if s1 in variables.keys():
                src = ~variables[s1]
            else:
                continue
            src = src % (2**16)
        case [s1, op, s2]:
            if s1 in variables.keys():
                s1 = variables[s1]
            else:
                try:
                    s1 = int(s1)
                except:
                    continue
            if s2 in variables.keys():
                s2 = variables[s2]
            else:
                try:
                    s2 = int(s2)
                except:
                    continue
            match op:
                case "AND": src = (s1 & s2) % (2**16)
                case "OR": src = (s1 | s2) % (2**16)
                case "RSHIFT": src = (s1 >> s2) % (2**16)
                case "LSHIFT": src = (s1 << s2) % (2**16)

    variables[dst] = src
    operations.remove(operations[(i-1) % len(operations)])

print(variables["a"])
