# Solution: 670

with open("input.txt", "r") as f:
    passwords = list(map(lambda x : x.strip(), f.readlines()))

counter = 0
for password in passwords:
    password = password.split(" ")
    first = int(password[0]) - 1
    second = int(password[1]) - 1
    char = password[2]
    password = password[3]
    valid = (1 if char == password[first] else 0) + (1 if char == password[second] else 0)
    counter += (1 if valid == 1 else 0)

print(counter)
