# Solution: 85555470

with open("input.txt", "r") as f:
    numbers = list(map(lambda x : int(x.strip()), f.readlines()))

numbers.sort()

for i in range(len(numbers)-2):
    for j in range(len(numbers)-1):
        found = False
        for t in range(len(numbers)):
            if numbers[i] + numbers[j] + numbers[t] == 2020:
                print(numbers[i] * numbers[j] * numbers[t])
                found = True
                break

        if found:
            break
    
    if found:
        break
