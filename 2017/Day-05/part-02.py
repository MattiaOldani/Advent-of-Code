# Solution: 28178177

with open("input.txt", "r") as f:
    jumps = f.readlines()

jumps = list(map(lambda x : int(x.strip()), jumps))

i = 0
counter = 0
while i < len(jumps):
    jump = jumps[i]
    jumps[i] += (1 if jump < 3 else -1)
    i += jump
    counter += 1

print(counter)
