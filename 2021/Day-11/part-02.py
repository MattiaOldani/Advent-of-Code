# Solution: 324

with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip(), f.readlines()))

octopuses = list()
for line in data:
    values = list()
    for value in line:
        values.append(int(value))
    octopuses.append(values)

step = 0
while True:
    for line in octopuses:
        for i in range(len(line)):
            line[i] += 1
    
    flashed = [[False for _ in range(len(octopuses[0]))] for _ in range(len(octopuses))]
    
    loop = True
    flash = 0
    while loop:
        for i in range(len(octopuses)):
            for j in range(len(octopuses)):
                if octopuses[i][j] > 9 and not flashed[i][j]:
                    if i > 0:
                        octopuses[i-1][j] += 1
                        if j > 0:
                            octopuses[i-1][j-1] += 1
                        if j < len(octopuses[0]) - 1:
                            octopuses[i-1][j+1] += 1
                    if i < len(octopuses) - 1:
                        octopuses[i+1][j] += 1
                        if j > 0:
                            octopuses[i+1][j-1] += 1
                        if j < len(octopuses[0]) - 1:
                            octopuses[i+1][j+1] += 1
                    if j > 0:
                        octopuses[i][j-1] += 1
                    if j < len(octopuses[0]) - 1:
                        octopuses[i][j+1] += 1
                    
                    flash += 1
                    flashed[i][j] = True

        check = True
        for i in range(len(octopuses)):
            for j in range(len(octopuses[i])):
                if octopuses[i][j] > 9 and not flashed[i][j]:
                    check = False
                    break
            if not check:
                break
        loop = not check

    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            if flashed[i][j]:
                octopuses[i][j] = 0

    step += 1

    if flash == len(octopuses) * len(octopuses[0]):
        break

print(step)
