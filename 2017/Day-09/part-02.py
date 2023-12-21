# Solution: 5601

with open("input.txt", "r") as f:
    stream = list(f.read().strip())

while "!" in stream:
    index = stream.index("!")
    stream.pop(index)
    stream.pop(index)

total = 0
while "<" in stream:
    start = stream.index("<")
    for i in range(start+1, len(stream)):
        if stream[i] == ">":
            end = i
            break
    
    total += (end-start-1)

    for _ in range(end-start+1):
        stream.pop(start)

print(total)
