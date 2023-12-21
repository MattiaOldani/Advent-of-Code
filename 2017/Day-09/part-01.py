# Solution: 11898

with open("input.txt", "r") as f:
    stream = list(f.read().strip())

while "!" in stream:
    index = stream.index("!")
    stream.pop(index)
    stream.pop(index)

while "<" in stream:
    start = stream.index("<")
    for i in range(start+1, len(stream)):
        if stream[i] == ">":
            end = i
            break
    
    for _ in range(end-start+1):
        stream.pop(start)

depth = 0
total = 0
for char in stream:
    if char == "{":
        depth += 1
    elif char == "}":
        total += depth
        depth -= 1

print(total)
