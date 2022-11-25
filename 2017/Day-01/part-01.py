# Solution: 1089

with open("input.txt", "r") as f:
    digits = f.readline().strip()

counter = 0
for i in range(len(digits)):
    if digits[i] == digits[(i+1) % len(digits)]:
        counter += int(digits[i])

print(counter)
