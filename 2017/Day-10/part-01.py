# Solution: 6909

with open("input.txt", "r") as f:
    sequence = [int(x) for x in f.read().strip().split(",")]


ll = [i for i in range(256)]
cp = 0
ss = 0

for length in sequence:
    if length > len(ll):
        continue

    start = cp
    end = (cp + length - 1) % len(ll)

    for i in range(length // 2):
        cs, ce = (start + i) % len(ll), (end - i) % len(ll)
        ll[cs], ll[ce] = ll[ce], ll[cs]

    cp = (cp + length + ss) % len(ll)
    ss = (ss + 1) % len(ll)

print(ll[0] * ll[1])
