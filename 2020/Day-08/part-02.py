# Solution: 761

def change_flow(instructions):
    pc = 0
    accumulator = 0

    visited = set()
    while pc < len(instructions):
        if pc in visited:
            return None
        
        visited.add(pc)
        instruction = instructions[pc]
        
        match instruction:
            case ["acc", n]:
                accumulator += int(n)
                pc += 1
            case ["jmp", n]:
                pc += int(n)
            case ["nop", _]:
                pc += 1
    
    return accumulator


with open("input.txt", "r") as f:
    instructions = list(map(lambda x : x.strip().split(" "), f.readlines()))

for i,instruction in enumerate(instructions):
    if instruction[0] == "acc":
        continue

    program_copy = instructions.copy()
    new_instruction = ["nop" if instruction[0] == "jmp" else "jmp", instruction[1]]
    program_copy[i] = new_instruction

    accumulator = change_flow(program_copy)

    if accumulator is not None:
        print(accumulator)
        break
