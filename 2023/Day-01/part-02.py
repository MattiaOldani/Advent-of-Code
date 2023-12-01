# Solution: 54980

with open("input.txt", "r") as f:
    data = list(map(lambda x : x.strip(), f.readlines()))

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

words = list(DIGITS.keys())

count = 0
for line in data:
    find = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            find.append(int(line[index]))
        else:
            for word in words:
                if line.startswith(word):
                    find.append(DIGITS[word])
                    break
        index += 1

    count += find[0]*10 + find[-1]
    
print(count)
