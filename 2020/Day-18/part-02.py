# Solution: 321176691637769

def evaluate(expression: list) -> str:
    while "+" in expression:
        expression_copy = list()
        for i in range(0, len(expression)-2, 2):
            first = expression[i]
            operation = expression[i+1]
            second = expression[i+2]
            if operation == "+":
                result = str(int(first) + int(second))
                expression_copy.append(result)
                for t in range(i+3, len(expression)):
                    expression_copy.append(expression[t])
                break
            else:
                expression_copy.extend([first, operation])
        expression = expression_copy.copy()
    
    return str(eval(" ".join(expression)))


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
