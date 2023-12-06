# Solution: 32607562

with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" "), f.readlines()))

distance = int("".join(data.pop()))
time = int("".join(data.pop()))

count = 0
for i in range(1, time):
    if i * (time - i) > distance:
        count += 1

print(count)
