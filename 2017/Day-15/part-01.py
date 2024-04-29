# Solution: 577

with open("input.txt", "r") as f:
    sa,sb = list(map(int, f.readlines()))

mod = 2147483647
ma,mb = 16807,48271

count = 0
for _ in range(40000000):
    na = (sa * ma) % mod
    nb = (sb * mb) % mod

    if bin(na)[::-1][:16] == bin(nb)[::-1][:16]:
        count += 1

    sa = na
    sb = nb

print(count)
