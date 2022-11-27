# Solution: 1929

with open("input.txt", "r") as f:
    range_ = f.readline().strip().split("-")

start = int(range_[0])
end = int(range_[1])

counter = 0
for i in range(start+1, end):
    valid = 0
    number = str(i)
    for t in range(len(number)-1):
        if number[t+1] >= number[t]:
            valid += 1
    
    for t in range(len(number)-1):
        if number[t] == number[t+1]:
            valid += 1
            break

    counter += (1 if valid == 6 else 0)

print(counter)
