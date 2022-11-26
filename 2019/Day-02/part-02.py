# Solution: 7610

with open("input.txt", "r") as f:
    program = f.readline().strip().split(",")

program = list(map(lambda x : int(x), program))

for i in range(100):
    found = False
    for j in range(100):
        running = [x for x in program]

        running[1] = i
        running[2] = j
        
        index = 0
        while running[index] != 99:
            opcode = running[index]
            match opcode:
                case 1:
                    s1 = running[index + 1]
                    s2 = running[index + 2]
                    dst = running[index + 3]
                    running[dst] = running[s1] + running[s2]
                case 2:
                    s1 = running[index + 1]
                    s2 = running[index + 2]
                    dst = running[index + 3]
                    running[dst] = running[s1] * running[s2]

            index += 4
        
        if running[0] == 19690720:
            print(100 * i + j)
            found  = True
            break

    if found:
        break
