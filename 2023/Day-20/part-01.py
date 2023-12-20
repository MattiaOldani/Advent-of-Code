# Solution: 861743850

from abc import ABC, abstractmethod
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

    def send(self, source: str, pulse: int) -> list[tuple]:
        self.inputs[source] = pulse
        state = 0 if all([i == 1 for i in self.inputs.values()]) else 1
        
        return [(d,state) for d in self.destinations]


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

low = 0
high = 0
for _ in range(1000):
    low += 1
    
    queue = Queue()
    queue.put(("button", 0, "broadcaster"))
    while not queue.empty():
        source, pulse, destination = queue.get()
        
        try:
            current_module = modules[destination]
        except KeyError:
            continue

        following = current_module.send(source, pulse)

        low += len(list(filter(lambda x : x[1] == 0, following)))
        high += len(list(filter(lambda x : x[1] == 1, following)))

        for element in following:
            queue.put((destination, element[1], element[0]))

print(low * high)
