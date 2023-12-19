# Solution: 130303473508222

from functools import reduce


class Rule:
    def __init__(self, name: str, rules: list[str], default: str) -> None:
        self.name = name
        self.rules = rules
        self.default = default
    
    def combinations(self, ranges: dict, rules: dict) -> int:
        if self.name == "R":
            return 0

        if self.name == "A":
            return reduce(lambda c,x: c * (x[1]-x[0]+1), ranges.values(), 1)

        count = 0
        for rule in self.rules:
            condition, next_ = rule.split(":")
            variable = condition[0]
            operator = condition[1]
            number = int(condition[2:])
            
            copy = dict([(var,rng.copy()) for var,rng in ranges.items()])
            if operator == "<":
                number -= 1
                copy[variable][1] = min(copy[variable][1], number)
                ranges[variable] = [copy[variable][1] + 1, ranges[variable][1]]
            else:
                number += 1
                copy[variable][0] = max(copy[variable][0], number)
                ranges[variable] = [ranges[variable][0], copy[variable][0] - 1]
            
            count += rules[next_].combinations(copy, rules)

        count += rules[self.default].combinations(ranges, rules)
        return count


with open("input.txt", "r") as f:
    raw_rules, _ = list(map(lambda x : x.strip().split("\n"), f.read().split("\n\n")))

rules = {"A": Rule("A", None, None), "R": Rule("R", None, None)}
for rule in raw_rules:
    rule = rule.split()
    name = rule.pop(0)
    default = rule.pop()
    rules[name] = Rule(name, rule, default)

start = rules["in"]

print(start.combinations(dict([(var, [1,4000]) for var in "xmas"]), rules))
