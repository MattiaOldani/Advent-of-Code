# Solution: 11780

with open("input.txt", "r") as f:
    commands = list(map(lambda x : x.strip().split(" "), f.readlines()))

i = 0
total = 0
cycle = 1
register = 1
while cycle <= 220:
    command = commands[i]
    
    if cycle % 40 == 20:
        total += (cycle * register)
    
    if command[0] == "noop":
        cycle += 1
    else:
        cycle += 1
        if cycle % 40 == 20:
            total += (cycle * register)
        cycle += 1
        register += int(command[1])
    
    i += 1

print(total)
