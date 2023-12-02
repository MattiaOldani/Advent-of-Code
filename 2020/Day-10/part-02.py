# Solution: 338510590509056

with open("input.txt", "r") as f:
    adapter = list(map(lambda x : int(x.strip()), f.readlines()))

adapter.sort()
max_value = adapter[-1]

arrangements = dict([[n,0] for n in adapter])
arrangements[0] = 1
for value in adapter:
    for key in arrangements.keys():
        if 1 <= value - key <= 3:
            arrangements[value] += arrangements[key]

print(arrangements[max_value])
