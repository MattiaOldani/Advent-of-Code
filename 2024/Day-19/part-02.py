# Solution: 705756472327497

from functools import lru_cache


@lru_cache
def get_combination(design: str, towels: tuple[str]):
    if len(design) == 0:
        return 1

    count = 0
    for towel in towels:
        if design.startswith(towel):
            count += get_combination(design.removeprefix(towel), towels)

    return count


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")


towels = tuple(data[0].strip().split())
designs = data[1].strip().split("\n")

count = 0
for design in designs:
    count += get_combination(design, towels)

print(count)
