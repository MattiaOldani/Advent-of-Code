# Solution: 6568

with open("input.txt", "r") as f:
    data = [
        list(filter(lambda x: x != "x", x.strip().split(","))) for x in f.readlines()
    ]


timestamp = int(data[0][0])
bus_IDs = [int(x) for x in data[1]]

count = (float("inf"), 0)
for bus_ID in bus_IDs:
    before = (timestamp // bus_ID) * bus_ID

    after = before + bus_ID - timestamp
    if after < count[0]:
        count = (after, after * bus_ID)

print(count[1])
