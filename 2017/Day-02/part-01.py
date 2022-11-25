# Solution: 45158

with open("input.txt", "r") as f:
    rows = f.readlines()

checksum = 0
for row in rows:
    numbers = [x for x in row.strip().split("\t") if x != ""]
    numbers = [int(x) for x in numbers]
    numbers.sort()
    checksum += (numbers[len(numbers)-1] - numbers[0])

print(checksum)
