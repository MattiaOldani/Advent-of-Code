# Solution: 22847

class Rule:
    def __init__(
        self, low: int, low_location: str, high: int, high_location: str
    ) -> None:
        self.low: int = low
        self.low_location: str = low_location
        self.high: int = high
        self.high_location: str = high_location


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" "), f.readlines()))

raw_rules = list(filter(
    lambda x : x[0] == "bot",
    data
))

rules = dict()
values = dict()
for raw_rule in raw_rules:
    bot = int(raw_rule[1])
    low_location = raw_rule[2]
    low = int(raw_rule[3])
    high_location = raw_rule[4]
    high = int(raw_rule[5])
    rules[bot] = Rule(low, low_location, high, high_location)
    values[bot] = list()
    values[low] = list()
    values[high] = list()

raw_values = list(filter(
    lambda x : x[0] == "value",
    data
))

for raw_value in raw_values:
    value = int(raw_value[1])
    bot = int(raw_value[3])
    if bot in values:
        values[bot].append(value)
    else:
        values[bot] = [value]

output = dict(((0,[]), (1,[]), (2,[])))
while True:
    start = None
    for bot,val in values.items():
        if len(val) == 2:
            start = bot
            break
    
    if start is None:
        break

    val = sorted(values[start])

    rule = rules[start]
    if rule.low_location == "bot":
        values[rule.low].append(val[0])
    elif rule.low in (0,1,2):
        output[rule.low].append(val[0])
    if rule.high_location == "bot":
        values[rule.high].append(val[1])
    elif rule.high in (0,1,2):
        output[rule.high].append(val[1])
    
    values[start] = list()

prod = 1
for value in output.values():
    prod *= value[0]

print(prod)
