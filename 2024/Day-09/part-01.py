# Solution: 6461289671426

with open("input.txt", "r") as f:
    data = list(map(int, f.readline().strip()))


memory = []
for i, cell in enumerate(data):
    memory += [i // 2 if i % 2 == 0 else "." for _ in range(cell)]

start = memory.index(".")
end = len(memory) - 1
while start < end:
    memory[start], memory[end] = memory[end], memory[start]

    start = memory.index(".")
    while memory[end] == "." and end >= 0:
        end -= 1

count = 0
for index, cell in enumerate(filter(lambda x: x != ".", memory)):
    count += index * cell

print(count)
