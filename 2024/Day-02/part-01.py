# Solution: 356

with open("input.txt", "r") as f:
    reports = [[int(y) for y in x.split()] for x in f.readlines()]

count = 0
for report in reports:
    if report == sorted(report) or report == sorted(report, reverse=True):
        difference_report = [
            abs(report[i + 1] - report[i]) for i in range(len(report) - 1)
        ]
        if all([1 <= x <= 3 for x in difference_report]):
            count += 1

print(count)
