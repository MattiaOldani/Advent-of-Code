# Solution: 1384

with open("input.txt", "r") as f:
    instructions = list(map(lambda x : x.strip().split(" "), f.readlines()))

pc = 0
accumulator = 0

visited = set()
while True:
    if pc in visited:
        break
    
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
        
print(accumulator)
