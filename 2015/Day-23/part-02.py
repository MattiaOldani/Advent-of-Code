# Solution: 247

with open("input.txt", "r") as f:
    program = list(map(lambda x : x.strip().split(" "), f.readlines()))

instructions = {
    "hlf" : lambda registry: registry // 2,
    "tpl" : lambda registry : registry * 3,
    "inc" : lambda registry : registry + 1,
    "jmp" : lambda pc, offset : pc + offset,
    "jie" : lambda pc, offset, value : pc + (offset if value % 2 == 0 else 1),
    "jio" : lambda pc, offset, value : pc + (offset if value == 1 else 1)
}

pc = 0
registers = dict((("a", 1), ("b", 0)))
while pc < len(program):
    instruction = program[pc]
    command = instruction[0]
    match command:
        case "hlf" | "tpl" | "inc":
            registry = instruction[1]
            value = registers[registry]
            registers[registry] = instructions[command](value)
            pc += 1
        case "jmp":
            offset = int(instruction[1])
            pc = instructions[command](pc, offset)
        case "jie" | "jio":
            registry = instruction[1]
            value = registers[registry]
            offset = int(instruction[2])
            pc = instructions[command](pc, offset, value)
        case _:
            break

print(registers)
