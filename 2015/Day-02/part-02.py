# Solution: 3842356

with open('input.txt', 'r') as f:
    presents = list(map(lambda x : x.strip().split('x'), f.readlines()))
    total = 0
    for p in presents:  
        p = list(map(lambda x : int(x), p))
        p.sort()
        total += (2 * (p[0] + p[1]) + p[0]*p[1]*p[2])
    print(total)
