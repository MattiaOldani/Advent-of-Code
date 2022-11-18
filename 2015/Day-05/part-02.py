# Solution: 55

def match_couple(start, message):
    counter = 0
    
    for i in range(start, len(message), 2):
        try:
            couple = line[i:i+2]
        except:
            pass
        else:
            if message.count(couple) >= 2:
                return True

    return False


with open("input.txt", "r") as f:
    lines = f.readlines()

    counter = 0
    for line in lines:
        accept = match_couple(0, line) or match_couple(1, line)

        for i in range(len(line)-2):
            triple = line[i:i+3]
            if triple[0] == triple[2]:
                break
        else:
            accept = False

        counter += 1 if accept else 0

    print(counter)
