# Solution: 765748

with open("input.txt", "r") as f:
    data = [[int(z) for z in [y[0], y[-1]]] for y in [x.split() for x in f.readlines()]]

left = sorted([x[0] for x in data])
right = sorted([x[1] for x in data])

print(sum([abs(left[i] - right[i]) for i in range(len(left))]))
