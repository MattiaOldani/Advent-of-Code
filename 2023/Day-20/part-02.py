# Solution: 247023644760071

from abc import ABC, abstractmethod
from collections import defaultdict
from functools import reduce
from queue import Queue


class Module(ABC):
    @abstractmethod
    def send(self, source: str, pulse: int) -> list[tuple]:
        pass


class Broadcaster(Module):
    def __init__(self, destinations: list[str]) -> None:
        self.destinations = destinations

    def send(self, source: str, pulse: int) -> list[tuple]:
        return [(d,pulse) for d in self.destinations]


class FlipFlop(Module):
    def __init__(self, destinations: list[str]) -> None:
        self.destinations = destinations
        self.state = 0

    def send(self, source: str, pulse: int) -> list[tuple]:
        if pulse == 1:
            return []

        self.state = 1 - self.state
        
        return [(d,self.state) for d in self.destinations]

    
class Conjunction(Module):
    def __init__(self, destinations: list[str], inputs: list[str]) -> None:
        self.destinations = destinations
        self.inputs = dict([(i,0) for i in inputs])
        self.state = None

    def send(self, source: str, pulse: int) -> list[tuple]:
        self.inputs[source] = pulse
        self.state = 0 if all([i == 1 for i in self.inputs.values()]) else 1
        
        return [(d,self.state) for d in self.destinations]


def high_pulse_cycle(modules: dict, starter: str, end_input: str) -> int:
    count = 0
    while True:
        count += 1
        
        queue = Queue()
        queue.put(("button", 0, "broadcaster"))
        
        while not queue.empty():
            source, pulse, destination = queue.get()
            
            try:
                current_module = modules[destination]
            except KeyError:
                continue
            
            following = current_module.send(source, pulse)
    
            for element in following:
                queue.put((destination, element[1], element[0]))
        
            if modules[end_input].state == 1:
                return count


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
    data = list(map(lambda x : x.strip().split(" -> "), f.readlines()))

sources, destinations = [d[0] for d in data], [d[1].split() for d in data]

modules = dict()
for source,destination in zip(sources, destinations):
    if source == "broadcaster":
        modules[source] = Broadcaster(destination)
        continue
    
    name = source[1:]
    
    if source.startswith("%"):
        modules[name] = FlipFlop(destination)
        continue
    
    inputs = [s[1:] for s,d in zip(sources,destinations) if name in d]
    
    modules[name] = Conjunction(destination, inputs)

STARTER = ["bt", "rc", "qs", "qt"]
INPUTS = ["rn", "mk", "dh", "vf"]

steps = []
for start,end_input in zip(STARTER, INPUTS):
    modules["broadcaster"].destinations = [start]
    steps.append(high_pulse_cycle(modules, start, end_input))

prime_numbers = primes(steps.pop())
for number in steps:
    other_primes = primes(number)
    for number,times in other_primes.items():
        prime_numbers[number] = max(prime_numbers[number], times)

print(reduce(lambda x,y: x * y[0]**y[1], prime_numbers.items(), 1))
