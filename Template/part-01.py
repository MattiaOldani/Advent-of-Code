# Solution: 

with open("test.txt", "r") as f:
    data = list(map(lambda x : x.strip(), f.readlines()))

print(data)
