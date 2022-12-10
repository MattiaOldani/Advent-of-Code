# Solution: PZULBAUA

with open("input.txt", "r") as f:
    commands = list(map(lambda x : x.strip().split(" "), f.readlines()))

pixel = 0
sprite = 1
drawing = str()
for command in commands:
    drawing += ("#" if pixel in [sprite-1, sprite, sprite+1] else ".")
    
    if command[0] == "addx":
        pixel = (pixel + 1) % 40
        if pixel == 0:
            drawing += "\n"

        drawing += ("#" if pixel in [sprite-1, sprite, sprite+1] else ".")

        sprite += int(command[1])
    
    pixel = (pixel + 1) % 40
    if pixel == 0:
            drawing += "\n"

print(drawing)

print(drawing.replace(".", " ").strip())
