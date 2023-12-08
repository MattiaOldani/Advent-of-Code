# Solution: 11309

with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

commands = list(data[0])

couples = dict()
for line in data[1].strip().split("\n"):
    source, left, right = line.split()
    couples[source] = (left, right)

index = 0
count = 0
start = "AAA"
while not start == "ZZZ":
    direction = 0 if commands[index] == "L" else 1
    start = couples[start][direction]
    index = (index + 1) % len(commands)
    count += 1

print(count)
