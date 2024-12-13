# Solution: 89013607072065

from scipy.optimize import linprog


with open("input.txt", "r") as f:
    machines = [
        [[int(z) for z in y.split()] for y in x.strip().split("\n")]
        for x in f.read().split("\n\n")
    ]


count = 0
for A, B, P in machines:
    Ax, Ay = A
    Bx, By = B
    Px, Py = P
    Px += 10000000000000
    Py += 10000000000000

    A_ub = [[Ax, Bx], [Ay, By], [-Ax, -Bx], [-Ay, -By]]
    b_ub = [Px, Py, -Px, -Py]

    c = [3, 1]

    results = linprog(c, A_ub, b_ub, bounds=(0, None), integrality=1)

    count += int(results.fun) if results.success else 0

print(count == 89013607072065)
