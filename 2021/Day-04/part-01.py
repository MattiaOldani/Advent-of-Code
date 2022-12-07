# Solution: 23177

with open("input.txt", "r") as f:
    bingo = list(map(lambda x : x.strip(), f.readlines()))

extract = list(map(int, bingo[0].split(",")))

boards = list()
current = list()

bingo = bingo[2:]
for line in bingo:
    if line == "":
        boards.append(current)
        current = []
    else:
        line = list(map(int, line.replace("  ", " ").split(" ")))
        current.append(line)
else:
    boards.append(current)

for number in extract:
    winner = False
    for board in boards:
        for line in board:
            found = False
            for i in range(len(line)):
                if line[i] == number:
                    line[i] = 0
                    found = True
                    break
            if found:
                break
                
        total = 0
        check = False
        columns = [[row[i] for row in board] for i in range(5)] 
        for i in range(5):
            line = board[i]
            column = columns[i]
            total += sum(line)
            if sum(line) == 0 or sum(column) == 0:
                check = True
        else:
            total *= number
        
        if check:
            print(total)
            winner = True
            break

    if winner:
        break
