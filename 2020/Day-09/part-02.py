# Solution: 9351526

with open("input.txt", "r") as f:
    numbers = list(map(lambda x : int(x.strip()), f.readlines()))

numbers_backup = numbers.copy()
preamble = [numbers.pop(0) for _ in range(25)]

found = False
while not found:
    current = numbers.pop(0)
    for i in range(len(preamble)-1):
        for j in range(i+1,len(preamble)):
            if preamble[i] + preamble[j] == current:
                found = True
                break
    
    if found:
        found = False
        preamble.pop(0)
        preamble.append(current)
    else:
        break

found = False
target = current
for i in range(len(numbers_backup)):
    for j in range(i+1,len(numbers_backup)+1):
        current = numbers_backup[i:j]
        if sum(current) == target:
            print(max(current) + min(current))
            found = True
            break
    
    if found:
        break
