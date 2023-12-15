# Solution: 265462

from collections import defaultdict


class Lens:
    def __init__(self, label: str, focal_length: int) -> None:
        self.label = label
        self.focal_length = focal_length
    
    def __eq__(self, other) -> bool:
        return self.label == other.label


class Hashmap:
    def __init__(self) -> None:
        self.boxes = defaultdict(lambda: [])
    
    def insert(self, box_number: int, lens: Lens) -> None:
        lenses = self.boxes[box_number]
        if lens in lenses:
            index = lenses.index(lens)
            lenses[index] = lens
        else:
            lenses.append(lens)

    def remove(self, box_number: int, lens: Lens) -> None:
        lenses = self.boxes[box_number]
        if lens in lenses:
            lenses.remove(lens)
    
    def focusing_power(self) -> int:
        count = 0
        
        items = list(filter(lambda x : len(x[1]) > 0, self.boxes.items()))
        for box_number,lenses in items:
            for index,lens in enumerate(lenses):
                count += (box_number+1) * (index+1) * (lens.focal_length)

        return count


with open("input.txt", "r") as f:
    words = f.read().strip().split(",")

hashmap = Hashmap()
for word in words:
    index = max(word.find("="), word.find("-"))
    label = word[:index]

    box_number = 0
    for character in label:
        box_number = ((box_number + ord(character)) * 17) % 256

    if word[index] == "=":
        focal_length = int(word[-1])
        hashmap.insert(box_number, Lens(label, focal_length))
    else:
        hashmap.remove(box_number, Lens(label, -1))

print(hashmap.focusing_power())
