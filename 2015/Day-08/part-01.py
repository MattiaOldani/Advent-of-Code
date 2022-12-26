# Solution: 1342

with open("input.txt", "r") as f:
    words = list(map(lambda x : x.strip(), f.readlines()))

data = 0
memory = 0
for word in words:
    memory += len(word)
    word = word[1:len(word)-1]

    i = 0
    while i < len(word):
        data += 1
        if word[i] == "\\":
            i += 4 if word[i+1] == "x" else 2
        else:
            i += 1

print(memory - data)
