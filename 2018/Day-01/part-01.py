# Solution: 531

with open("input.txt", "r") as f:
    freq = f.readlines()

print(sum(list(map(lambda x : int(x.strip()), freq))))
