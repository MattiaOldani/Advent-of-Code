# Solution: 239727793813

class Field:
    def __init__(self, name: str, range_1: list, range_2: list) -> None:
        self.name = name
        self.range_1 = range(range_1[0], range_1[1]+1)
        self.range_2 = range(range_2[0], range_2[1]+1)
    
    def is_valid(self, number: int) -> bool:
        return number in self.range_1 or number in self.range_2


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

fields = list()

raw_fields = data.pop(0).split("\n")
for line in raw_fields:
    line = line.split(" ")
    name = line[0]
    range_1 = list(map(int, line[1].split("-")))
    range_2 = list(map(int, line[3].split("-")))
    fields.append(Field(name, range_1, range_2))

count = 0
tickets = data.pop().split("\n")[::-1][1:][::-1] + [data.pop()]

valid_tickets = list()
for ticket in tickets:
    valid = True
    values = list(map(int, ticket.split(",")))
    for value in values:
        if all(map(lambda x : not x.is_valid(value), fields)):
            valid = False
            break
    
    if valid:
        valid_tickets.append(values)
    
personal_ticket = valid_tickets[-1]
valid_fields = dict(zip([f.name for f in fields], [[] for _ in range(len(fields))]))

for i in range(len(valid_tickets[0])):
    column = [t[i] for t in valid_tickets]
    for field in fields:
        if all(map(lambda x : field.is_valid(x), column)):
            valid_fields[field.name].append(i)

count = 1
while len(valid_fields) > 0:
    single = list(filter(lambda x : len(x[1]) == 1, valid_fields.items()))[0]
    
    name = single[0]
    position = single[1][0]
    del valid_fields[single[0]]

    if name.startswith("departure"):
        count *= personal_ticket[position]
    
    for positions in valid_fields.values():
        positions.remove(position)

print(count)
