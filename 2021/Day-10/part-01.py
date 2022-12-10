# Solution: 345441

with open("input.txt", "r") as f:
    lines = list(map(lambda x : x.strip(), f.readlines()))

POINTS = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

total = 0
for line in lines:
    stack = list()
    for char in line:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        else:
            if stack.pop()+char not in ["()", "[]", "{}", "<>"]:
                total += POINTS[char]
                break
    
print(total)
