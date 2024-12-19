# Solution: 3,6,7,0,5,7,3,1,4

with open("input.txt", "r") as f:
    a, b, c = [int(x.split()[1]) for x in f.read().split("\n\n")[0].split("\n")]


output = []
while a > 0:
    b = a % 8
    b = b ^ 1
    c = a // 2**b
    b = b ^ 5
    b = b ^ c
    output += [b % 8]
    a = a // 8

print(",".join([str(o) for o in output]))
