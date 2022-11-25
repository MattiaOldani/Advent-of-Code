# Solution: 294

with open("input.txt", "r") as f:
    rows = f.readlines()

checksum = 0
for row in rows:
    numbers = [x for x in row.strip().split("\t") if x != ""]
    numbers = [int(x) for x in numbers]
    numbers.sort()

    found = False
    for i in range(len(numbers)-1):
        if found:
            break
        for j in range(i+1, len(numbers)):
            if numbers[i] % numbers[j] == 0:
                found = True
                checksum += numbers[i] / numbers[j]
                break
            elif numbers[j] % numbers[i] == 0:
                found = True
                checksum += numbers[j] / numbers[i]
                break

print(checksum)
