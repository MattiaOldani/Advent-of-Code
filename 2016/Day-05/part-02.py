# Solution: 999828ec

import hashlib

with open("input.txt", "r") as f:
    id_ = f.readline().strip()

index = 0
counter = 0
psw = ["_" for i in range(8)]
while psw.count("_") > 0:
    code = id_ + str(index)
    digest = hashlib.md5(code.encode()).hexdigest()
    if digest[:5] == "00000":
        try:
            position = int(digest[5])
            if 0 <= position <= 7 and psw[position] == "_":
                psw[position] = digest[6]
                print(' '.join([str(x) for x in psw]))
        except:
            pass
    index += 1

print(f"\nPassword: {''.join([str(x) for x in psw])}")
