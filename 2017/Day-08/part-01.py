# Solution: 2971

from collections import defaultdict


with open("input.txt", "r") as f:
    instructions = list(map(lambda x : x.strip().split(" if "), f.readlines()))

registers = defaultdict(lambda: 0)
for instruction in instructions:
    instruction, condition = instruction[0].split(), instruction[1].split()
    condition[0] = f"registers['{condition[0]}']"
    condition = " ".join(condition)
    
    if eval(condition):
        match instruction:
            case [register, "inc", value]:
                registers[register] += int(value)
            case [register, "dec", value]:
                registers[register] -= int(value)
            case _:
                pass
    
print(max(registers.values()))
