# Solution: 1068

with open("input.txt", "r") as f:
    sequences = list(map(lambda x : [int(y) for y in x.strip().split()], f.readlines()))

count = 0
for sequence in sequences:
    step = [sequence]
    current = sequence
    while not all([c == 0 for c in current]):
        new_step = [current[i+1]-current[i] for i in range(len(current)-1)]
        step.append(new_step)
        current = new_step

    step.reverse()
    step[0].insert(0, 0)
    for i,current in enumerate(step[:len(step)-1]):
        first = current[0]
        step[i+1].insert(0, step[i+1][0] - first)
    
    count += step[-1][0]

print(count)
