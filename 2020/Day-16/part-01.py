# Solution: 23115

class Field:
    def __init__(self, range_1: list, range_2: list) -> None:
        self.range_1 = range(range_1[0], range_1[1]+1)
        self.range_2 = range(range_2[0], range_2[1]+1)
    
    def is_valid(self, number: int) -> bool:
        return number in self.range_1 or number in self.range_2


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

fields = list()

raw_fields = data.pop(0).split("\n")
for line in raw_fields:
    line = line.split(" ")[1:]
    range_1 = list(map(int, line[0].split("-")))
    range_2 = list(map(int, line[2].split("-")))
    fields.append(Field(range_1, range_2))

count = 0
tickets = data.pop().split("\n")[::-1][1:][::-1]
for ticket in tickets:
    values = list(map(int, ticket.split(",")))
    for value in values:
        if all(map(lambda x : not x.is_valid(value), fields)):
            count += value

print(count)
