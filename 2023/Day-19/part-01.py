# Solution: 342650

class Part:
    def __init__(self, x: int, m: int, a: int, s: int) -> None:
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    
    def rating(self) -> int:
        return self.x + self.m + self.a + self.s


class Rule:
    def __init__(self, name: str, rules: list[str], default: str) -> None:
        self.name = name
        self.rules = rules
        self.default = default
    
    def apply(self, part: Part, rules: dict) -> int:
        if self.name == "R":
            return 0

        if self.name == "A":
            return part.rating()

        for rule in self.rules:
            condition, next_ = rule.split(":")
            condition = "part." + condition
            if eval(condition):
                return rules[next_].apply(part, rules)
        
        return rules[self.default].apply(part, rules)


with open("input.txt", "r") as f:
    raw_rules, raw_parts = list(map(lambda x : x.strip().split("\n"), f.read().split("\n\n")))

rules = {"A": Rule("A", None, None), "R": Rule("R", None, None)}
for rule in raw_rules:
    rule = rule.split()
    name = rule.pop(0)
    default = rule.pop()
    rules[name] = Rule(name, rule, default)

start = rules["in"]

count = 0
for part in raw_parts:
    x,m,a,s = list(map(int, part.split()))
    part = Part(x, m, a, s)
    count += start.apply(part, rules)

print(count)
