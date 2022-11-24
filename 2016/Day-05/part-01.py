# Solution: f77a0e6e

import hashlib

with open("input.txt", "r") as f:
    id_ = f.readline().strip()

index = 0
psw = str()
while len(psw) < 8:
    code = id_ + str(index)
    digest = hashlib.md5(code.encode()).hexdigest()
    if digest[:5] == "00000":
        psw += digest[5]
    index += 1

print(psw)
