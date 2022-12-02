# Solution: 6782

with open("input.txt", "r") as f:
    forms = list(map(lambda x : x.strip().replace("\n", "") , f.read().split("\n\n")))

total = 0
for form in forms:
    while len(form) > 0:
        current = form[0]
        form = form.replace(current, "")
        total += 1
    
print(total)
