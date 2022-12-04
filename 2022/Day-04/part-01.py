# Solution: 576

with open("input.txt", "r") as f:
    couples = list(map(lambda x : x.strip().split(","), f.readlines()))

full = 0
for couple in couples:
    first = list(map(int, couple[0].split("-")))
    second = list(map(int, couple[1].split("-")))
    if first[0] <= second[0] and first[1] >= second[1]:
        full += 1   
    elif second[0] <= first[0] and second[1] >= first[1]:
        full += 1

print(full)
