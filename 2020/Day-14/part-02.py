# Solution: 4215284199669

from itertools import combinations_with_replacement, permutations


class Bitmask:
    def __init__(self) -> None:
        self.mask = None
    
    def set_mask(self, mask: str) -> None:
        self.mask = mask

    def apply_mask(self, bits: str) -> list[str]:
        result = str()
        for mask,bit in zip(self.mask, bits):
            if mask == "0":
                result += bit
            else:
                result += mask
        
        x_number = result.count("X")
        combinations = combinations_with_replacement(["0","1"], x_number)
        
        results = list()
        for combination in combinations:
            all_combinations = set(permutations(combination))
            for combination in all_combinations:
                fill = str()
                blocks = result.split("X")
                last = blocks.pop()
                for i,block in enumerate(blocks):
                    fill += block + combination[i]
                fill += last
                results.append(int(fill, 2))

        return results


    def __len__(self) -> int:
        return len(self.mask)


def convert(number: str, bit_number: int) -> str:
    bits = bin(int(number)).split("b")[1]
    return "0"*(bit_number - len(bits)) + bits


with open("input.txt", "r") as f:
    operations = list(map(lambda x : x.strip().split(" "), f.readlines()))

memory = dict()
bitmask = Bitmask()

for operation in operations:
    if len(operation) == 1:
        bitmask.set_mask(operation[0])
        continue
    
    bit_number = len(bitmask)
    destination = convert(operation.pop(0), bit_number)
    destinations = bitmask.apply_mask(destination)

    value = int(operation.pop())
    for destination in destinations:
        memory[destination] = value

print(sum(value for value in memory.values()))
