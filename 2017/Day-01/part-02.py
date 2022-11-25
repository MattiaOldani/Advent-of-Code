# Solution: 1156

with open("input.txt", "r") as f:
    digits = f.readline().strip()

counter = 0
shift = int(len(digits) / 2)
for i in range(len(digits)):
    if digits[i] == digits[(i+shift) % len(digits)]:
        counter += int(digits[i])

print(counter)
