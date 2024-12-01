# Solution: 27732508

with open("input.txt", "r") as f:
    data = [[int(z) for z in [y[0], y[-1]]] for y in [x.split() for x in f.readlines()]]

left = [x[0] for x in data]
right = [x[1] for x in data]

count = [right.count(l) for l in left]

print(sum([left[i] * count[i] for i in range(len(left))]))
