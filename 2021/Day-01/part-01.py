# Solution: 1548

with open("input.txt", "r") as f:
    measures = list(map(lambda x : int(x.strip()), f.readlines()))

print(sum([1 for i in range(1,len(measures)) if measures[i] > measures[i-1]]))
