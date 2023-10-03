# Solution: 9227657

with open("input.txt", "r") as f:
    program = list(map(lambda x : x.strip().split(" "), f.readlines()))

registers = dict(
    (("a",0), ("b",0), ("c",1), ("d",0))
)

instructions = {
    "cpy" : lambda x : x,
    "inc" : lambda x : x + 1,
    "dec" : lambda x : x - 1,
    "jnz" : lambda x, y : y if x != 0 else 1
}

pc = 0
while pc < len(program):
    current_instruction = program[pc]
    command = current_instruction[0]
    match command:
        case "cpy":
            src = current_instruction[1]
            try:
                src = int(src)
            except Exception:
                src = registers[src]
            dst = current_instruction[2]
            registers[dst] = instructions[command](src)
            pc += 1
        case "inc" | "dec":
            dst = current_instruction[1]
            registers[dst] = instructions[command](registers[dst])
            pc += 1
        case "jnz":
            check = current_instruction[1]
            try:
                check = int(check)
            except Exception:
                check = registers[check]
            offset = int(current_instruction[2])
            pc += instructions[command](check, offset)
        case _:
            break

print(registers)
