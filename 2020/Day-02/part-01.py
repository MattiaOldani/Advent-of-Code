# Solution: 666

with open("input.txt", "r") as f:
    passwords = list(map(lambda x : x.strip(), f.readlines()))

counter = 0
for password in passwords:
    password = password.split(" ")
    min_ = int(password[0])
    max_ = int(password[1])
    char = password[2]
    password = password[3]
    counter += (1 if min_ <= password.count(char) <= max_ else 0)

print(counter)
