# Solution: 255

VOWELS = "aeiou"

SKIP = [
    "ab", "cd", "pq", "xy"
]

with open("input.txt", "r") as f:
    lines = f.readlines()

    counter = 0
    for line in lines:
        vowels = sum([1 for char in line if char in VOWELS])
        
        accept = False
        for i in range(len(line)-1):
            couple = line[i:i+2]
            if couple in SKIP:
                accept = False
                break
            if couple[0] == couple[1]:
                accept = True

        if accept and vowels >= 3:
            counter += 1

    print(counter)
