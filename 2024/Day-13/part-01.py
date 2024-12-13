# Solution: 32026

import subprocess


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

    with open("data.dat", "w") as f:
        f.write("param nB := 2;\n\n")
        f.write("param nD := 2;\n\n")

        f.write(f"param Movements: 1 2 :=\n1 {Ax} {Bx}\n2 {Ay} {By};\n\n")

        f.write(f"param Targets :=\n1 {Px}\n2 {Py};\n\n")

        f.write("param TokenPrices :=\n1 3\n2 1;\n")

    results = (
        subprocess.check_output(
            ["ampl", "part-01.run"],
            stderr=subprocess.DEVNULL,
        )
        .decode("utf-8")
        .strip()
        .split("\n")
    )

    if len(results) == 3:
        count += int(results[-1].split()[-1])

print(count)
