# Solution: 9d5f4561367d379cfbf04f8c471c0095

from functools import reduce


def fancy_hash(sequence):
    ll = [i for i in range(256)]
    cp = 0
    ss = 0

    for _ in range(64):
        cp, ss = round(ll, sequence, cp, ss)

    return sparse_2_dense(ll)


def sparse_2_dense(ll):
    result = ""

    for i in range(16):
        block = ll[i * 16 : (i + 1) * 16]
        result += format(reduce(lambda x, y: x ^ y, block, 0), "#04x")[2:]

    return result


def round(ll, sequence, cp, ss):
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

    return cp, ss


with open("input.txt", "r") as f:
    sequence = [ord(x) for x in f.read().strip()] + [17, 31, 73, 47, 23]


print(fancy_hash(sequence))
