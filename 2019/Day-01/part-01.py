# Solution: 3234871

with open("input.txt", "r") as f:
    fuel = f.readlines()

print(sum(list(map(lambda x : int(int(x.strip()) / 3) - 2, fuel))))
