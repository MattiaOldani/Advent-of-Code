# Solution: 3596

with open("input.txt", "r") as f:
    forms = list(map(lambda x : x.strip().split("\n"), f.read().split("\n\n")))

total = 0
for form in forms:
    if len(forms) == 1:
        total += len(form)
    else:
        required = len(form)
        form = ''.join(form)
        while len(form) > 0:
            current = form[0]
            if form.count(current) == required:
                total += 1
            form = form.replace(current, "")
    
print(total)
