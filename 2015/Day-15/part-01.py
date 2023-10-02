# Solution: 21367368

from itertools import combinations_with_replacement, permutations


class Ingredient:
    def __init__(
        self,
        capacity: int,
        durability: int,
        flavor: int,
        texture: int
    ) -> None:
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
    

class Cookie:
    def __init__(self, ingredients: list[Ingredient]) -> None:
        self.ingredients = ingredients.copy()
    
    def score(self, quantity: list[int]) -> int:
        capacity = 0
        durability = 0
        flavor = 0
        texture = 0
        for i,ingredient in enumerate(self.ingredients):
            capacity += ingredient.capacity * quantity[i]
            durability += ingredient.durability * quantity[i]
            flavor += ingredient.flavor * quantity[i]
            texture += ingredient.texture * quantity[i]
        capacity = capacity if capacity > 0 else 0
        durability = durability if durability > 0 else 0
        flavor = flavor if flavor > 0 else 0
        texture = texture if texture > 0 else 0
        return capacity * durability * flavor * texture


with open("input.txt", "r") as f:
    raw_ingredients = list(map(lambda x : x.strip().split(" "), f.readlines()))

ingredients = list()
for line in raw_ingredients:
    name = line[0]
    capacity = int(line[2])
    durability = int(line[4])
    flavor = int(line[6])
    texture = int(line[8])
    ingredients.append(Ingredient(
        capacity, durability, flavor, texture
    ))

cookie = Cookie(ingredients)

max_ = 0
values = [i for i in range(0,101)]
for combination in combinations_with_replacement(values, len(ingredients)):
    if sum(combination) == 100:
        for permutation in permutations(combination):
            max_ = max(max_, cookie.score(permutation))

print(max_)
