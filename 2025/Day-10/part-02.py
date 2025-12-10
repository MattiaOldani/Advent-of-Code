# Solution: 18105

from ortools.sat.python import cp_model


with open("input.txt", "r") as f:
    data = [x.strip().split()[1:] for x in f.readlines()]

model = cp_model.CpModel()

count = 0
for line in data:
    levels = list(map(int, line.pop()[1:-1].split(",")))

    buttons = list(map(lambda x: list(map(int, x[1:-1].split(","))), line))

    vars = [
        model.NewIntVar(0, max(levels), f"{i:02}_presses") for i in range(len(buttons))
    ]

    for i in range(len(levels)):
        model.Add(sum([v for t, v in enumerate(vars) if i in buttons[t]]) == levels[i])

    model.Minimize(sum(vars))

    solver = cp_model.CpSolver()
    result = solver.Solve(model)

    count += int(solver.ObjectiveValue())

print(count)
