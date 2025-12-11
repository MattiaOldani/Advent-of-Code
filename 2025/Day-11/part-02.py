# Solution: 473741288064360


def path(current: str, target: str, graph: dict[str, str], depth: int):
    if depth == 0:
        return 1 if current == target else 0

    if current == target:
        return 1

    count = 0
    for neighbor in graph[current]:
        count += path(neighbor, target, graph, depth - 1)

    return count


with open("input.txt", "r") as f:
    data = [x.strip().replace(":", "").split() for x in f.readlines()]

graph = {}
for line in data:
    graph[line[0]] = line[1:]

count = 1
for src, dst, depth in [("svr", "fft", 9), ("fft", "dac", 17), ("dac", "out", 10)]:
    count *= path(src, dst, graph, depth)

print(count)
