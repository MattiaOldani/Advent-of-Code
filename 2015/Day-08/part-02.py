# Solution: 2074

with open("input.txt", "r") as f:
    words = list(map(lambda x : x.strip(), f.readlines()))

data = 0
memory = 0
for word in words:
    data += len(word)
    memory += (len(word) + 4)
    word = word[1:len(word)-1]

    i = 0
    while i < len(word):
        if word[i] == "\\":
            memory += 1 if word[i:i+2] == "\\x" else 2
            i += 2
        else:
            i += 1

print(memory - data)
