# Solution: 3938038

from hashlib import md5

with open('input.txt', 'r') as f:
    key = f.readline()
    n = 0
    while True:
        current_key = key + str(n)
        if md5(current_key.encode()).hexdigest()[:6] == '000000':
            print(n)
            break
        n += 1
