# Solution: 905

with open("input.txt", "r") as f:
    couples = list(map(lambda x : x.strip().split(","), f.readlines()))

overlap = 0
for couple in couples:
    first = list(map(int, couple[0].split("-")))
    second = list(map(int, couple[1].split("-")))
    all = [x for x in range(first[0], first[1]+1)]
    all.extend([x for x in range(second[0], second[1]+1)])
    no_dup = set(all)
    if len(all) != len(no_dup):
        overlap += 1

print(overlap)
