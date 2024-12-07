# Solution: 169122112716571

from itertools import product


with open("input.txt", "r") as f:
    data = [
        [int(x.split(": ")[0]), list(map(int, x.split()[1:]))] for x in f.readlines()
    ]


operators = [lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))]

count = 0
for test, equation in data:
    repeat = len(equation) - 1
    for combination in product(operators, repeat=repeat):
        a = equation[0]
        for i in range(len(equation) - 1):
            a = combination[i](a, equation[i + 1])
            if a > test:
                break

        if test == a:
            count += test
            break

print(count)
