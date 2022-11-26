# Solution: 3765464

with open("input.txt", "r") as f:
    program = f.readline().strip().split(",")

program = list(map(lambda x : int(x), program))

program[1] = 12
program[2] = 2

index = 0
while program[index] != 99:
    opcode = program[index]

    match opcode:
        case 1:
            s1 = program[index + 1]
            s2 = program[index + 2]
            dst = program[index + 3]
            program[dst] = program[s1] + program[s2]
        case 2:
            s1 = program[index + 1]
            s2 = program[index + 2]
            dst = program[index + 3]
            program[dst] = program[s1] * program[s2]

    index += 4

print(program[0])
