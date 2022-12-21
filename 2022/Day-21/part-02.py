# Solution: 3759569926192

class Monkey():
    def __init__(self, name, waiting, operation, opposite, number):
        self.name = name
        self.waiting = waiting
        self.operation = operation
        self.opposite = opposite
        self.number = number
        self.is_final = False if number == None else True


def normal_evaluation(monkes, current):
    if current.is_final:
        return current.number
    
    first = monkeys[current.waiting[0]]
    second = monkeys[current.waiting[1]]

    return int(current.operation(normal_evaluation(monkeys,first), normal_evaluation(monkeys,second)))


def evaluation(monkeys, current, known):
    left = monkeys[current.waiting[0]]
    right = monkeys[current.waiting[1]]

    if find(monkeys, left):
        value = normal_evaluation(monkeys, right)
        next = left
        index = 0
    else:
        value = normal_evaluation(monkeys, left)
        next = right
        index = 1
    
    known = current.opposite[index](value, known)
    
    return known if next.name == "humn" else evaluation(monkeys, next, known)


def find(monkeys, current):
    if current.is_final:
        return current.name == "humn"
    
    first = monkeys[current.waiting[0]]
    second = monkeys[current.waiting[1]]

    return find(monkeys,first) or find(monkeys,second)


with open("input.txt", "r") as f:
    tree = list(map(lambda x : x.strip().split(": "), f.readlines()))

monkeys = dict()
for node in tree:
    name = node[0]
    waiting = node[1].split(" ")
    if len(waiting) == 1:
        monkeys[name] = Monkey(name, None, None, None, int(node[1]))
    else:
        match waiting[1]:
            case "+":
                operation = lambda x,y : x + y
                opposite = [lambda x,y : y - x] * 2
            case "-":
                operation = lambda x,y : x - y
                opposite = [lambda x,y : x + y, lambda x,y : - y + x]
            case "*":
                operation = lambda x,y : x * y
                opposite = [lambda x,y : y // x] * 2
            case "/":
                operation = lambda x,y : x // y
                opposite = [lambda x,y : x * y, lambda x,y : (y // x)**(-1)]
        monkeys[name] = Monkey(name, [waiting[0], waiting[2]], operation, opposite, None)
else:
    monkeys["root"].operation = lambda x,y : x == y

root = monkeys["root"]

if find(monkeys,monkeys[root.waiting[0]]):
    known = normal_evaluation(monkeys, monkeys[root.waiting[1]])
    location = monkeys[root.waiting[0]]
else:
    known = normal_evaluation(monkeys, monkeys[root.waiting[0]])
    location = monkeys[root.waiting[1]]

print(evaluation(monkeys, location, known))
