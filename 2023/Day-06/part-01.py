# Solution: 503424

with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" "), f.readlines()))

distances = list(map(int, data.pop()))
times = list(map(int, data.pop()))

count = 1
for time,distance in zip(times, distances):
    valid = 0
    for i in range(1, time):
        if i * (time - i) > distance:
            valid += 1

    count *= valid

print(count)
