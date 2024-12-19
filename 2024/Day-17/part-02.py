# Solution: 164278496489149


def exec_program(a):
    b, c = 0, 0

    output = []
    while a > 0:
        b = a % 8
        b = b ^ 1
        c = a // 2**b
        b = b ^ 5
        b = b ^ c
        output += [b % 8]
        a = a // 8

    return output


with open("input.txt", "r") as f:
    program = [int(x) for x in f.read().split("\n\n")[1].strip().split(",")]


starters = set([0])
for instruction in program[::-1]:
    new_starters = set()
    for start in starters:
        start *= 8
        for t in range(start, start + 8):
            output = exec_program(t)

            if output and output[0] == instruction:
                new_starters.add(t)

    starters = new_starters

print(min(starters))
