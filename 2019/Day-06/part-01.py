# Solution: 300598


def number_of_orbits(planets, current):
    if current == "COM":
        return 0

    return 1 + number_of_orbits(planets, planets[current])


with open("input.txt", "r") as f:
    data = [x.strip().split(")") for x in f.readlines()]


planets = {}
for start, end in data:
    planets[end] = start

count = 0
for planet in planets.keys():
    count += number_of_orbits(planets, planet)

print(count)
