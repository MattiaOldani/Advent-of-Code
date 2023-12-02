# Solution: 332

class Bag:
    def __init__(self, name: str, other_bags: list) -> None:
        self.name = name
        self.other_bags = other_bags
    
    def has_gold_bag(self) -> bool:
        names = [bag.name for bag in self.other_bags]
        if "shiny_gold" in names:
            return True
        
        for bag in self.other_bags:
            if bag.has_gold_bag():
                return True
        
        return False


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" "), f.readlines()))

names = set()
for line in data:
    for i in range(0, len(line), 2):
        names.add(line[i])

bags = dict()
for name in names:
    bags[name] = Bag(name, [])

for line in data:
    name = line.pop(0)
    other_bags = list()
    for i in range(1, len(line), 2):
        other_bags.append(bags[line[i]])
    bags[name].other_bags = other_bags

count = 0
for bag in bags.values():
    if bag.has_gold_bag():
        count += 1

print(count)
