# Solution: 10875

class Bag:
    def __init__(self, name: str, other_bags: list, quantity: list) -> None:
        self.name = name
        self.other_bags = other_bags
        self.quantity = quantity

    def count_bags(self) -> int:
        if len(self.other_bags) == 0:
            return 0

        count = sum(self.quantity)
        for bag,n in zip(self.other_bags, self.quantity):
            count += (n * bag.count_bags())
  
        return count


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" "), f.readlines()))

names = set()
for line in data:
    for i in range(0, len(line), 2):
        names.add(line[i])

bags = dict()
for name in names:
    bags[name] = Bag(name, [], [])

for line in data:
    name = line.pop(0)
    other_bags = list()
    quantity = list()
    for i in range(0, len(line), 2):
        quantity.append(int(line[i]))
        other_bags.append(bags[line[i+1]])
    bags[name].other_bags = other_bags
    bags[name].quantity = quantity

gold = bags["shiny_gold"]
print(gold.count_bags())
