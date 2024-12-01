# Solution:

with open("test.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

print(data)
