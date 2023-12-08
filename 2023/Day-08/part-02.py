# Solution: 13740108158591

from collections import defaultdict
from functools import reduce


def primes(number: int) -> dict:
    prime_numbers = defaultdict(lambda: 0)
    while number > 1:
        for d in range(2, number+1):
            if number % d == 0:
                prime_numbers[d] += 1
                number = number // d
                break
    return prime_numbers


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

commands = list(data[0])

couples = dict()
for line in data[1].strip().split("\n"):
    source, left, right = line.split()
    couples[source] = (left, right)

starts = [c for c in couples.keys() if c.endswith("A")]
ends = dict([(c, []) for c in couples.keys() if c.endswith("Z")])

index = 0
count = 0
while not all([len(e)>=1 for e in ends.values()]):
    count += 1

    direction = 0 if commands[index] == "L" else 1
    for i in range(len(starts)):
        start = starts[i]
        end = couples[start][direction]
        if end.endswith("Z"):
            ends[end].append(count)
        starts[i] = end
    
    index = (index + 1) % len(commands)

prime_numbers = primes(list(ends.popitem())[1][0])
for number in ends.values():
    other_primes = primes(number[0])
    for number,times in other_primes.items():
        prime_numbers[number] = max(prime_numbers[number], times)

print(reduce(lambda x,y: x * y[0]**y[1], prime_numbers.items(), 1))
