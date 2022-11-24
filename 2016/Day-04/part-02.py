# Solution: 993

with open("input.txt", "r") as f:
    rooms = f.readlines()

for room in rooms:
    fields = room.strip().split("-")
    words = fields[:len(fields)-1]

    char = dict()
    for word in words:
        for ch in word:
            try:
                char[ch] += 1
            except:
                char[ch] = 1
    occ = list(char.items())
    occ.sort(key=lambda x : x[0])
    occ.sort(key=lambda x : x[1], reverse=True)

    checksum = fields[len(fields)-1].split("[")[1]
    checksum = checksum[:len(checksum)-1]
    mine = str()
    for i in range(len(checksum)):
        mine += occ[i][0]

    if mine == checksum:
        key = int(fields[len(fields)-1].split("[")[0])
        key = key % 26
        dec = str()
        for ch in room:
            if ch == "-":
                dec += " "
            else:
                code = ord(ch) + key
                if code > 122:
                    code -= 26
                dec += chr(code)
        
        if "northpole" in dec:
            print(int(fields[len(fields)-1].split("[")[0]))
            break
