# Solution: 510009915468

def evaluate(expression: list) -> str:
    while len(expression) > 1:
        first = int(expression.pop(0))
        operation = expression.pop(0)
        second = int(expression.pop(0))
        if operation == "+":
            expression.insert(0, str(first + second))
        else:
            expression.insert(0, str(first* second))
    
    return expression[0]


with open("input.txt", "r") as f:
    expressions = list(map(lambda x : x.strip(), f.readlines()))

count = 0
for expression in expressions:
    while "(" in expression:
        start = 0
        tokens = expression.split(" ")
        for i,token in enumerate(tokens):
            if token == "(":
                start = i
            elif token == ")":
                result = evaluate(tokens[start+1:i].copy())
                expression = expression.replace(" ".join(tokens[start:i+1]), result)
                break
    
    count += int(evaluate(expression.split(" ")))

print(count)
