# Solution: 14839536808842

class Bitmask:
    def __init__(self) -> None:
        self.mask = None
    
    def set_mask(self, mask: str) -> None:
        self.mask = mask

    def apply_mask(self, bits: str) -> str:
        result = str()
        for mask,bit in zip(self.mask, bits):
            if mask == "X":
                result += bit
            else:
                result += mask
        
        return result

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
    
    destination = int(operation.pop(0))
    bit_number = len(bitmask)
    value = convert(operation.pop(), bit_number)

    memory[destination] = bitmask.apply_mask(value)

print(sum(int(value,2) for value in memory.values()))
