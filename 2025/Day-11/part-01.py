# Solution: 696


def path_to_out(current: str, graph: dict[str, str]):
    if current == "out":
        return 1

    count = 0
    for neighbor in graph[current]:
        count += path_to_out(neighbor, graph)

    return count


with open("input.txt", "r") as f:
    data = [x.strip().replace(":", "").split() for x in f.readlines()]

graph = {}
for line in data:
    graph[line[0]] = line[1:]

print(path_to_out("you", graph))
