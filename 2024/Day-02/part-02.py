# Solution: 413


def check_sorting(report) -> bool:
    return report == sorted(report) or report == sorted(report, reverse=True)


def check_difference(report) -> bool:
    difference_report = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
    return all([1 <= x <= 3 for x in difference_report])


with open("input.txt", "r") as f:
    reports = [[int(y) for y in x.split()] for x in f.readlines()]

count = 0
for report in reports:
    if check_sorting(report):
        if check_difference(report):
            count += 1
            continue
        else:
            for i in range(len(report)):
                short_report = report[:i] + report[i + 1 :]
                if check_difference(short_report):
                    count += 1
                    break
    else:
        for i in range(len(report)):
            short_report = report[:i] + report[i + 1 :]
            if check_sorting(short_report) and check_difference(short_report):
                count += 1
                break

print(count)
