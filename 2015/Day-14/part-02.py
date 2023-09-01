# Solution: 1059

class Reindeer():
    def __init__(self, velocity, fly_time, rest_time):
        self.velocity = velocity
        self.fly_time = fly_time
        self.rest_time = rest_time
        self.extra = 0
        self.distance = 0
        self.fly_count = 0
        self.rest_count = 0
        self.rest = False
    
    def step(self):
        if self.rest:
            self.rest_count += 1
            if self.rest_count == self.rest_time:
                self.rest = False
                self.rest_count = 0
        else:
            self.distance += self.velocity
            self.fly_count += 1
            if self.fly_count == self.fly_time:
                self.rest = True
                self.fly_count = 0

    def extra_point(self):
        self.extra += 1


with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip().split(" "), f.readlines()))

reindeers = list()
for line in data:
    reindeers.append(Reindeer(
        int(line[1]),
        int(line[2]),
        int(line[3])
    ))

i = 0
while i <= 2503:
    for reindeer in reindeers:
        reindeer.step()
    current_max = max([r.distance for r in reindeers])
    for reindeer in reindeers:
        if reindeer.distance == current_max:
            reindeer.extra_point()
    i += 1

print(max(r.extra for r in reindeers))
