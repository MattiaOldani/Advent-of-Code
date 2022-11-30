# Solution: 902451

with open("input.txt", "r") as f:
    numbers = list(map(lambda x : int(x.strip()), f.readlines()))

numbers.sort()

for i in range(len(numbers)-1):
    found = False
    for j in range(len(numbers)):
        if numbers[i] + numbers[j] == 2020:
            print(numbers[i] * numbers[j])
            found = True
            break
    
    if found:
        break
