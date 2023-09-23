# Solution: ZBJAB

with open("input.txt", "r") as f:
    data = list(f.read().strip())

WIDTH = 25
HEIGHT = 6
STEP = WIDTH * HEIGHT

screen = list()
for i in range(STEP):
    pixels = [data[t] for t in range(i, len(data), STEP)]
    
    while len(pixels) >= 0 and pixels[0] == "2":
        pixels.pop(0)

    if pixels[0] == "1":
        screen.append("#")
    else:
        screen.append(" ")
        
for _ in range(HEIGHT):
    for _ in range(WIDTH):
        print(screen.pop(0), end="")
    print()
