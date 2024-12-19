# Solution: 304

from functools import lru_cache


@lru_cache
def is_valid(design: str, towels: tuple[str]):
    if len(design) == 0:
        return True

    valid = False
    for towel in towels:
        if design.startswith(towel):
            valid |= is_valid(design.removeprefix(towel), towels)

    return valid


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")


towels = tuple(data[0].strip().split())
designs = data[1].strip().split("\n")

count = 0
for design in designs:
    count += int(is_valid(design, towels))

print(count)
