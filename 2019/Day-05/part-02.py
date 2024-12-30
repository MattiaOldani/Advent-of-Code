# Solution: 8805067


def pad(start: str, upper: int) -> str:
    return (upper - len(start)) * "0" + start


def get_operand(positions: list[int], index: int, mode: str) -> int:
    return positions[positions[index]] if mode == "0" else positions[index]


with open("input.txt", "r") as f:
    program = [int(x) for x in f.readline().strip().split(",")]


OPERATIONS = {"01": lambda x, y: x + y, "02": lambda x, y: x * y}
CHECK_JUMP = {"05": lambda x: x != 0, "06": lambda x: x == 0}
CHECK = {"07": lambda x, y: x < y, "08": lambda x, y: x == y}

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
            program[dst] = 5
            index += 2
        case "04":
            modes = pad(modes, 1)[::-1]
            src = get_operand(program, index + 1, modes[0])
            print(f"Diagnostic code: {src}")
            index += 2
        case "05" | "06":
            modes = pad(modes, 2)[::-1]
            check = get_operand(program, index + 1, modes[0])
            final = get_operand(program, index + 2, modes[1])
            index = final if CHECK_JUMP[opcode](check) else index + 3
        case "07" | "08":
            modes = pad(modes, 2)[::-1]
            first = get_operand(program, index + 1, modes[0])
            second = get_operand(program, index + 2, modes[1])
            dst = program[index + 3]
            program[dst] = 1 if CHECK[opcode](first, second) else 0
            index += 4
