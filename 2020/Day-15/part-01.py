# Solution: 387

from collections import defaultdict


with open("input.txt", "r") as f:
    first_numbers = list(map(int, f.readline().strip().split(",")))

numbers = defaultdict(lambda: -1)

turn = 1
last = first_numbers.pop()
for number in first_numbers:
    numbers[number] = turn
    turn += 1

while turn < 2020:
    cit = numbers[last]
    numbers[last] = turn
    if cit == -1:
        last = 0
    else:
        difference = turn - cit
        last = difference

    turn += 1

print(last)
