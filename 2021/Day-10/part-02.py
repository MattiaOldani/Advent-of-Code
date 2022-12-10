# Solution: 3235371166

with open("input.txt", "r") as f:
    lines = list(map(lambda x : x.strip(), f.readlines()))

POINTS = {
    "(" : 1,
    "[" : 2,
    "{" : 3,
    "<" : 4
}

scores = list()
for line in lines:
    stack = list()
    corrupted = False
    for char in line:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        else:
            if stack.pop()+char not in ["()", "[]", "{}", "<>"]:
                corrupted = True
                break
    
    if corrupted:
        continue

    total = 0
    while len(stack) > 0:
        total = (5 * total) + POINTS[stack.pop()]
    
    scores.append(total)

scores.sort()
print(scores[len(scores) // 2])
