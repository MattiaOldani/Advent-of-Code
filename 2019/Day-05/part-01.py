# Solution: 8332629


def pad(start: str, upper: int) -> str:
    return (upper - len(start)) * "0" + start


def get_operand(positions: list[int], index: int, mode: str) -> int:
    return positions[positions[index]] if mode == "0" else positions[index]


with open("input.txt", "r") as f:
    program = [int(x) for x in f.readline().strip().split(",")]


OPERATIONS = {"01": lambda x, y: x + y, "02": lambda x, y: x * y}

index = 0
while program[index] != 99:
    opcode = pad(str(program[index]), 2)

    modes, opcode = opcode[:-2], opcode[-2:]

    match opcode:
        case "01" | "02":
            modes = pad(modes, 2)[::-1]
            s1 = get_operand(program, index + 1, modes[0])
            s2 = get_operand(program, index + 2, modes[1])
            dst = program[index + 3]
            program[dst] = OPERATIONS[opcode](s1, s2)
            index += 4
        case "03":
            dst = program[index + 1]
            program[dst] = 1
            index += 2
        case "04":
            modes = pad(modes, 1)[::-1]
            src = get_operand(program, index + 1, modes[0])
            print(f"Diagnostic code: {src}")
            index += 2
