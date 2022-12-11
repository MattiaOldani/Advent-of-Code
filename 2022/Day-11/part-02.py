# Solution: 14106266886

class Monkey():
    def __init__(self, id_, items, operation, test, true, false):
        self.id_ = id_
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.total = 0


with open("input.txt", "r") as f:
    shit = list(map(lambda x : x.strip().split("\n"), f.read().split("\n\n")))

modulo = 1
monkeys = list()
for block in shit:
    id_ = int(block[0].strip().split(":")[0].split(" ")[1])
    items = list(map(int, block[1].strip().split(": ")[1].split(", ")))
    operation = block[2].strip().split(": ")[1].split(" = ")[1]
    test = int(block[3].strip().split(" ")[3])
    modulo *= test
    true = int(block[4].strip().split(" ")[5])
    false = int(block[5].strip().split(" ")[5])
    monkeys.append(Monkey(id_, items, operation, test, true, false))

for i in range(10000):
    for monkey in monkeys:
        items = monkey.items
        monkey.total += len(items)
        while len(items) > 0:
            old = items.pop()
            new = eval(monkey.operation) % modulo
            if new % monkey.test == 0:
                monkeys[monkey.true].items.append(new)
            else:
                monkeys[monkey.false].items.append(new)
    
score = [monkey.total for monkey in monkeys]
score.sort(reverse=True)

print(score[0] * score[1])
