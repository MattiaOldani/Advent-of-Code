# Solution: 84244467642604

class Monkey():
    def __init__(self, name, waiting, operation, number):
        self.name = name
        self.waiting = waiting
        self.operation = operation
        self.number = number
        self.is_final = False if number == None else True


def evaluation(monkeys, current):
    if current.is_final:
        return current.number
    
    first = monkeys[current.waiting[0]]
    second = monkeys[current.waiting[1]]

    return current.operation(evaluation(monkeys,first), evaluation(monkeys,second))


with open("input.txt", "r") as f:
    tree = list(map(lambda x : x.strip().split(": "), f.readlines()))

monkeys = dict()
for node in tree:
    name = node[0]
    waiting = node[1].split(" ")
    if len(waiting) == 1:
        monkeys[name] = Monkey(name, None, None, int(node[1]))
    else:
        match waiting[1]:
            case "+": operation = lambda x,y : x + y
            case "-": operation = lambda x,y : x - y
            case "*": operation = lambda x,y : x * y
            case "/": operation = lambda x,y : x // y
        monkeys[name] = Monkey(name, [waiting[0], waiting[2]], operation, None)

print(evaluation(monkeys, monkeys["root"]))
