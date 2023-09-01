# Solution: 2655

with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" "), f.readlines()))

distance = 0
for reindeer in data:
    velocity = int(reindeer[1])
    fly_time = int(reindeer[2])
    rest_time = int(reindeer[3])
    clock = 0
    count = 0
    while clock <= 2503:
        i = 0
        while clock <= 2503 and i < fly_time:
            count += velocity
            clock += 1
            i += 1
        clock += rest_time
    distance = max(distance, count)

print(distance)
