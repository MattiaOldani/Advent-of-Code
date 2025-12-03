# Solution: 172981362045136

with open("input.txt", "r") as f:
    data = [list(map(int, x.strip())) for x in f.readlines()]

count = 0
for line in data:
    weights = [0 for _ in range(len(line))]
    couples = list(zip(line, weights))
    couples = list(map(list, couples))

    for i in range(12):
        start = 0
        end = len(line)

        while True:
            max_value = max(couples[start:end], key=lambda x: x[0] * (1 - x[1]))
            index = couples.index(max_value)

            if i == 11:
                break

            if sum([1 - x[1] for x in couples[index + 1 :]]) < 12 - i - 1:
                end = index
                continue

            break

        for i in range(index):
            if couples[i][0] < max_value[0] and couples[i][1] == 0:
                couples[i][1] = 100

        couples[index][1] = 1

    count += int(
        "".join(map(lambda x: str(x[0]), filter(lambda x: x[1] == 1, couples)))
    )

print(count)
