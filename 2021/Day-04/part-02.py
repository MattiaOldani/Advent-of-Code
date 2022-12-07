# Solution: 6804

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

i = 0
while len(boards) > 0:
    number = extract[i]
    
    remove = list()
    for board in boards:
        for line in board:
            found = False
            for t in range(len(line)):
                if line[t] == number:
                    line[t] = 0
                    found = True
                    break
            if found:
                break
                
        total = 0
        check = False
        columns = [[row[t] for row in board] for t in range(5)]
        for t in range(5):
            line = board[t]
            column = columns[t]
            total += sum(line)
            if sum(line) == 0 or sum(column) == 0:
                check = True
        else:
            total *= number

        if check:
            remove.append(board)

    for r in remove:
        boards.remove(r)
    
    i += 1

print(total)
