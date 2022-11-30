# Solution: 1559

with open("input.txt", "r") as f:
    measures = list(map(lambda x : int(x.strip()), f.readlines()))

counter = 0
previous = sum(measures[0:3])
for i in range(3,len(measures)):
    current = previous - measures[i-3] + measures[i]
    counter += (1 if current > previous else 0)
    previous = current

print(counter)
