# Solution: 32607562

with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" "), f.readlines()))

distance = int("".join(data.pop()))
time = int("".join(data.pop()))

'''
Soluzione da matematico

lower = math.ceil(time - math.sqrt(time ** 2 - 4 * distance) / 2)
upper = math.floor(time + math.sqrt(time ** 2 - 4 * distance) / 2)

print(upper - lower)
'''

count = 0
for i in range(1, time):
    if i * (time - i) > distance:
        count += 1

print(count)
