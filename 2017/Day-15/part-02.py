# Solution: 316

with open("input.txt", "r") as f:
    sa,sb = list(map(int, f.readlines()))

mod = 2147483647
ma,mb = 16807,48271

count = 0
for i in range(5000000):
    while True:
        na = (sa * ma) % mod
        if na % 4 == 0:
            break
        sa = na
    
    while True:
        nb = (sb * mb) % mod
        if nb % 8 == 0:
            break
        sb = nb
    
    if bin(na)[::-1][:16] == bin(nb)[::-1][:16]:
        count += 1

    sa = na
    sb = nb

print(count)
