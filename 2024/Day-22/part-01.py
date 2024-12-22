# Solution: 13461553007

with open("input.txt", "r") as f:
    starters = [int(x.strip()) for x in f.readlines()]

count = 0
for starter in starters:
    for _ in range(2000):
        starter = ((starter * 64) ^ starter) % 16777216
        starter = ((starter // 32) ^ starter) % 16777216
        starter = ((starter * 2048) ^ starter) % 16777216

    count += starter

print(count)
