# Solution: 522

from ortools.sat.python import cp_model


with open("input.txt", "r") as f:
    data = [x.strip().split()[:-1] for x in f.readlines()]

model = cp_model.CpModel()

count = 0
for line in data:
    lights = list(map(lambda x: 1 if x == "#" else 0, line.pop(0)[1:-1]))

    buttons = list(map(lambda x: list(map(int, x[1:-1].split(","))), line))

    vars = [model.NewBoolVar(f"Press_{i:02}") for i in range(len(buttons))]

    for i in range(len(lights)):
        off = lights[i] == 0
        model.AddBoolXOr([v for t, v in enumerate(vars) if i in buttons[t]] + [off])

    model.Minimize(sum(vars))

    solver = cp_model.CpSolver()
    result = solver.Solve(model)

    count += int(solver.ObjectiveValue())

print(count)
