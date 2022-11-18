# Solution: 1795

with open('input.txt', 'r') as f:
    movements = f.readline()
    counter = 0
    for i in range(len(movements)):
        counter += 1 if movements[i] == '(' else -1
        if counter == -1:
            print(i+1)
            break
