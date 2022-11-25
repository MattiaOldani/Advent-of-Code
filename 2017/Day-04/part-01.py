# Solution: 466

with open("input.txt", "r") as f:
    passwords = f.readlines()

counter = 0
for password in passwords:
    words = password.strip().split(" ")
    words.sort()

    dup = False
    for i in range(len(words)-1):
        if words[i] == words[i+1]:
            dup = True
            break
    
    if not dup:
        counter += 1

print(counter)
